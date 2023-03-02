import os
import time
from functools import wraps
from flask import request
from dataclasses import dataclass
import asyncio
from okta_jwt_verifier import JWTVerifier
from okta_jwt_verifier.exceptions import JWTValidationException


TOKEN_CACHE = {}

ISSUER = 'https://{}/oauth2/default'.format(os.getenv('OKTA_DOMAIN'))
CLIENT_ID = os.getenv('OKTA_CLIENT_ID')

@dataclass
class TokenData:
    kid: str
    alg: str
    ver: int
    jti: str
    iss: str
    aud: str
    iat: int
    exp: int
    cid: str
    uid: str
    scp: list
    auth_time: int
    sub: str
    jwt_signature: bytes
    jwt_header: dict


def _parse_token(token: str):
    jwt_verifier = JWTVerifier(ISSUER, CLIENT_ID, 'api://default')
    return(jwt_verifier.parse_token(token))

async def _validate_token(token: str):
    jwt_verifier = JWTVerifier(ISSUER, CLIENT_ID, 'api://default')
    try:
        result = await jwt_verifier.verify_access_token(token)
        return {
            "status": "ok",
            "message": result,
        }
    except JWTValidationException as e:
        return {
            "status": "ko",
            "message": getattr(e, 'message', repr(e))
        }

async def _authenticate(token: str):
    # token validation
    validation_result = await _validate_token(token)

    # if token is ok then trying to get user details
    if validation_result['status'] == 'ok':
        token_parsing_result = _parse_token(token)
        return {
            "validation_result": validation_result,
            "token_parsing_result": token_parsing_result
        }
    else:
        return {
            "validation_result": validation_result,
            "token_parsing_result": None
        }

def validate_token(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Check if the Authorization header is present
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return {'message': 'Authorization header is missing'}, 401

        # Check if the header starts with 'Bearer '
        auth_header_parts = auth_header.split()
        if len(auth_header_parts) != 2 or auth_header_parts[0] != 'Bearer':
            return {'message': 'Invalid Authorization header'}, 401

        # Extract the token from the header
        token = auth_header_parts[1]

        # Check if token is already validated and not expired
        if token in TOKEN_CACHE:
            token_data = TOKEN_CACHE[token]
            if time.time() < token_data.exp:
                # Call the function
                return f(*args, username=token_data.sub, **kwargs)
            else:
                # Remove expired token from cache
                del TOKEN_CACHE[token]

        print('Invoking OKTA...')
        result = asyncio.run(_authenticate(token))

        if result['validation_result']['status'] == 'ok':
            header, payload, signature, _ = result['token_parsing_result']
            token_data = TokenData(
                kid=header['kid'],
                alg=header['alg'],
                ver=payload['ver'],
                jti=payload['jti'],
                iss=payload['iss'],
                aud=payload['aud'],
                iat=payload['iat'],
                exp=payload['exp'],
                cid=payload['cid'],
                uid=payload['uid'],
                scp=payload['scp'],
                auth_time=payload['auth_time'],
                sub=payload['sub'],
                jwt_signature=signature,
                jwt_header=header
            )

            # Store token in cache
            TOKEN_CACHE[token] = token_data

            # Call the function
            return f(*args, username=token_data.sub, **kwargs)
        
        else:
            return {'message': 'Invalid or expired token. Please log in again.'}, 401

    return decorated_function
