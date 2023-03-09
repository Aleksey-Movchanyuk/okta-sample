
```
sudo apt install python3-virtualenv
virtualenv venv
source venv/bin/activate

python setup.py sdist
```



```
venv\Scripts\activate

$Env:JWT="...token for validation..."

python token_validation.py
```

```
$Env:FLASK_APP="api"
$Env:FLASK_ENV="test"
```