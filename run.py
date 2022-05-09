from app import app

if __name__ == "__main__":
    PORT = 5001
    app.run(port=PORT)

# bash
#export FLASK_APP=run.py
#export FLASK_ENV=development
#export FLASK_RUN_PORT = 8080
#flask run

## windows - ps
# $Env:FLASK_APP = "run.py"
# $Env:FLASK_ENV = "development"
# $Env:FLASK_RUN_PORT = "8080"
#flask run