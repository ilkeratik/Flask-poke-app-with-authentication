from app import app
from flask import request, render_template,redirect, session, jsonify
from functools import wraps
import requests

from db.database import db
from db.mongodb import db as mdb

from models.search_results_model import SearchResult

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

@app.route('/dashboard/pokemon/<name>', methods=[ 'GET' ])
@login_required
def get_poke(name):
    descrip_url = f"https://pokeapi.co/api/v2/pokemon-species/{name}"
    r = requests.get(descrip_url)
    if r.status_code != 200:
        return jsonify({'message': "Couldn't find that pokemon!", 'status': 404}), 404
    json_blob = r.json()
    flav_text = extract_descriptive_text(json_blob)
    return jsonify({'message': "Got the pokemon", 'status': 200,'name': name, 'description': flav_text}), 200

def extract_descriptive_text(json_blob, language='en'):
    text = []
    for f in json_blob['flavor_text_entries']:
        if f['language']['name'] == language:
            text.append(f['flavor_text'])
    return text

@app.route('/dashboard/save_result', methods=[ 'POST' ])
@login_required
def save_result_to_db():
    print('hi')
    post_body = request.get_json()
    print(post_body)
    new_res = SearchResult(**post_body)
    resp = new_res.save()
    
    return f'Successfully added block to blockchain, data={post_body} ', 200