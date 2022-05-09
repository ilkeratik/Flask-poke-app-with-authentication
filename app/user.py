from app import app
from flask import request, render_template, redirect, session, jsonify
from models.user_model import User
from passlib.hash import pbkdf2_sha256
from db.database import db

@app.route('/')
def index():
    return render_template('public/index.html')

@app.route('/login',methods=[ 'GET' ])
def login():
    return render_template('public/login.html')

@app.route('/user/register', methods=[ 'POST' ])
def register_new_user():
    try:
        post_body = request.form
        username = post_body['username']
        email = post_body['email']
        password = post_body['password'] 
        print(post_body)
        new_user = User()
        new_user.username = username
        new_user.email = email
        new_user.password = pbkdf2_sha256.encrypt(password)
        print(len(new_user.password))
        db.session.add(new_user)
        try:
            db.session.commit()
        except Exception as e:
            return {
                'message': "Couldn't register the user.",
                'status': 400,
                'Error': str(e.args[0]),
            }, 400
        
        return {
                'message': f'Successfully registered the user, username={username}',
                'status': 200
            }, 200
    except Exception as e:
        return e, 500

@app.route('/user/login', methods=[ 'POST' ])
def login_user():
    try:
        post_body = request.form
        email = post_body['email']
        password = post_body['password'] 
        user = User.query.filter_by(email=email).first()
        if user is None:
            return {
                'message': "No matching user with given email.",
                'status': 401
            }, 401

        elif pbkdf2_sha256.verify(password , user.password):
            return start_session(user)
            # return redirect("/dashboard", code=302)

        else:
            return {
                'message': "Wrong login credentials.",
                'status': 401
            }, 401
    except Exception as e:
        return e, 500
        
@app.route('/user/signout')
def signout():
    session.clear()
    return redirect('/')

def start_session(user):
    try:
        print(session)
        user.password = None
        
        session['logged_in'] = True
        session['user'] = {
            "username": user.username,
            "email": user.email
        }
        print(session)
        return {
                'user': session['user'],
                'message': f'Successfully registered the user, username',
                'status': 200
            }, 200
    except Exception as e:
        return e, 500
    