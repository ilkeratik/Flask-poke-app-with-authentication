from app import app
from flask import request, render_template,redirect, session
from user_model import User

from database import db

from functools import wraps

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')

    return wrap
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('authenticated_user/dashboard.html')
