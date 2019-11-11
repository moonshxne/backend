from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
from pymongo import MongoClient
import json
from flask_cors import CORS
import bcrypt


client = MongoClient('localhost', 27017)
db = client["hackenger"]
users = db["users"]
app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'mongodb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017' #need URL
mongo = PyMongo(app)
CORS(app)

@app.route('/')
def index():
#    the_dictionary = request.data
#    username = the_dictionary.keys()
#    password = request.data.values()
#    collection.insert(the_dictionary)
#    if username in session:
#        return ('You\'re logged in!', list_of_contacts)
#    return render_template('index.html')
	pass

@app.route('/Login', methods=['POST'])
def login():
	combination = json.loads(request.data)
	#print(combination['un'])
	#print(combination['pw'])

	user = (combination['un'])
	passwords = (combination['pw'])

	users.find()
	# for x in users.keys():
	# 	print(x)
		#list_of_users.append(x)
		#login_user = users.find_one({'name' : request.form[user]}) #need variable
		# if login_user:
			# if bcrypt.hashpw(request.form['passwords'].encode('utf-8'), login_user[user].encode('utf-8')) == login_user[''].encode('utf-8'):
				# session[user] = request.form[user]
				# return redirect(url_for('index'))
	return 'Invalid username/password'
	# return request.data

@app.route('/Signup', methods=['POST', 'GET'])
def register_user():
	# if request.method == 'POST':
	# 	users = mongo.db.users
	# 	existing_user = users.find_one({'name' : request.form[username]})
	# 	if existing_user is None:
	# 		hashpass = bcrypt.hashpw(request.form[username].encode('utf-8'), bcrypt.gensalt())
	# 		users.insert({'name' : request.form[username], '' : hashpass})
	# 		session[username] = request.form[username]
	# 		return redirect(url_for('index'))
	# return render_template('register.html')
	pass

@app.route('/Chat', methods=['POST', 'GET'])
def chat():
	# if request.method == 'POST':
	# 	message_and_user = request.data
	# 	message = message_and_user.keys()
	# 	user_to_talk_to = message_and_user.values()
	# 	collection.insert(message_and_user)
	# return message_and_user
	pass

if __name__ == '__main__':
	app.secret_key = 'mysecret'
	app.run(debug=True)