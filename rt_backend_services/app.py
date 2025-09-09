
from flask import Flask, jsonify, request, Blueprint
from config import mongo_uri
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)


client = MongoClient(mongo_uri)
db = client['User_data']
collection = db['User_info']

@app.route('/new_user', methods=['GET', 'POST'])
def register():
	if request.method == 'POST':
		req_data = request.get_json()
		username = req_data.get('username')
		password = req_data.get('password')
		hashed_password = generate_password_hash(password)
		result = collection.insert_one({ "username": username, "password": hashed_password })
		return jsonify({"success": True, "inserted_id": str(result.inserted_id)})
	return jsonify({"success": False, "message": "Invalid method"}), 405

@app.route('/user', methods=['POST'])
def login():
	req_data = request.get_json()
	username = req_data.get('username')
	password = req_data.get('password')
	user = collection.find_one({'username': username})
	if user and check_password_hash(user['password'], password):
		return jsonify({"success": True})
	else:
		return jsonify({"success": False}), 401

if __name__ == '__main__':
	app.run( debug=True, host='0.0.0.0')