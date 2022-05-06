from app import app
from flask import Flask, jsonify, request, render_template
from user_model import User

from database import db

@app.route('/')
def index():
    return render_template('public/index.html')

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
        new_user.password = password
        db.session.add(new_user)
        try:
            db.session.commit()
        except Exception as e:
            return {
                'message': "Couldn't register the user.",
                'status': 400,
                'Error': str(e.args[0]),
            }, 400
        
        return f'Successfully registered the user, username={username} ', 200
    except Exception as e:
        return e, 500

