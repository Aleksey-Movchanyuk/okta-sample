## OKTA integration sample

* Angular 13 - Frontend
* Flask/Python 3.11 - Backend

### OKTA DEV


| Key            | Value                 |
|----------------|-----------------------|
| OKTA_DOMAIN    | dev-43780148.okta.com |
| OKTA_CLIENT_ID | 0oa8kak1syywzL5o15d7  |


### OKTA PROD


| Key            | Value                 |
|----------------|-----------------------|
| OKTA_DOMAIN    | dev-43780148.okta.com |
| OKTA_CLIENT_ID | 0oa5uj9kwdMhBfhyV5d7  |


### Steps that needs to be done

```
New-Alias -name python -Value C:\home\python3111x64\python.exe

python -m pip install --upgrade pip

python -m pip uninstall wfastcgi

python -m pip install wfastcgi
python -m pip install flask
python -m pip install flask_cors
python -m pip install okta_jwt_verifier

$Env:PATH += ";C:\home\python3111x64\Scripts"
```

### Angular Build Commands

#### Development environment
```
ng build
```

#### Production environment
```
ng build --configuration=production
```