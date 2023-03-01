import os
import asyncio

import argparse

from okta_jwt_verifier import JWTVerifier
from okta_jwt_verifier.exceptions import JWTValidationException


ISSUER = 'https://{}/oauth2/default'.format(os.getenv('OKTA_DOMAIN'))
CLIENT_ID = os.getenv('OKTA_CLIENT_ID')


def authentication(token: str):
    # token validation
    loop = asyncio.get_event_loop()
    validation_result = loop.run_until_complete(validate_token(token))

    # if token is ok then trying to get user details
    if validation_result['status'] == 'ok':
        token_parsing_result = parse_token(token)
        return {
            "validation_result": validation_result,
            "token_parsing_result": token_parsing_result
        }
    else:
        return {
            "validation_result": validation_result,
            "token_parsing_result": None
        }


async def validate_token(token: str):
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

def parse_token(token: str):
    jwt_verifier = JWTVerifier(ISSUER, CLIENT_ID, 'api://default')
    return(jwt_verifier.parse_token(token))


if __name__ == "__main__":
    # Define the expected command-line arguments
    parser = argparse.ArgumentParser(description='Process a token value.')
    parser.add_argument('--token', type=str, help='The token value to process.')
    
    # Parse the command-line arguments
    args = parser.parse_args()
    
    # Extract the token value from the parsed arguments
    token = args.token

    result = authentication(token)
    print(result)
