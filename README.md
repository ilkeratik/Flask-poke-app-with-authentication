**Running the application**

*Bash*
```
export FLASK_APP=run.py
export FLASK_ENV=development
export FLASK_RUN_PORT = 8080
```
*Powershell*
```
$Env:FLASK_APP = "run.py"
$Env:FLASK_ENV = "development"
$Env:FLASK_RUN_PORT = "8080"
```
Then
```
flask run
```

**Install all packages**
```
pip3 install -r requirements.txt
```
