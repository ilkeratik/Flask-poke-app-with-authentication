from app import app

if __name__ == "__main__":
    PORT = 5001
    app.run(port=PORT)

#export FLASK_APP=run.py
#export FLASK_ENV=development