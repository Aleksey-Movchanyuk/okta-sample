
# Prerequisites

## Linux

```
sudo apt install python3-virtualenv
virtualenv venv
source venv/bin/activate
```

## MacOS

```
pip install virtualenv
virtualenv venv
source venv/bin/activate
```

## Windows

```
python -m pip install --user virtualenv
virtualenv venv
venv\Scripts\activate
```

# Commands

## Install requirements

```
python setup.py sdist
pip install ./dist/okta-sample-backend-1.0.tar.gz
``` 

## Token validation

```
$Env:JWT="...token for validation..."
python token_validation.py
```

## Run the Flask app

```
$Env:FLASK_APP="api"
flask run
```
