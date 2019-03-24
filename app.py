import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
from config import dbconfig
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.secret_key = "randomstring123"


app.config["MONGO_DBNAME"] = 'recipe_manager'
app.config["MONGO_URI"] = dbconfig()

mongo = PyMongo(app)

"""See if user is in session and print message out if they are in session"""
"""If user is not in session then send them to index page"""

users_collection = mongo.db.register
recipes_collection = mongo.db.recipes

# Collections

users_collection = mongo.db.users
recipes_collection = mongo.db.recipes

@app.route('/')
@app.route('/index')

def index():
    return render_template("index.html")

"""
User AUTH
"""

# Login

@app.route('/login', methods=['GET'])
def login():
	# Check if user is not logged in already
	if 'user' in session:
		user_in_db = users_collection.find_one({"username": session['user']})
		
		if user_in_db:
			# If so redirect user to his profile
			flash("You are logged in already!")
			return redirect(url_for('profile', user=user_in_db['username']))
			
		else:
			# Render the page for user to be able to log in
			return render_template("login.html")
			# Check user login details from login form

@app.route('/user_auth', methods=['POST'])
def user_auth():
	form = request.form.to_dict()
	user_in_db = users_collection.find_one({"username": form['username']})
	# Check for user in database
	
	if user_in_db:
		# If passwords match (hashed / real password)
		if check_password_hash(user_in_db['password'], form['user_password']):
			# Log user in (add to session)
			session['user'] = form['username']
			
			# If the user is admin redirect him to admin area
			if session['user'] == "admin":
				return redirect(url_for('admin'))
				
			else:
				flash("You were logged in!")
				return redirect(url_for('profile', user=user_in_db['username']))
		
		else:
			flash("Wrong password or user name!")
			return redirect(url_for('login'))

	else:
		flash("You must be registered!")
		return redirect(url_for('register'))



# Sign up

@app.route('/register', methods=['GET', 'POST'])

def register():
	# Check if user is not logged in already
	if 'user' in session:
		flash('You are already signed in!')
		return redirect(url_for('index'))
		

	if request.method == 'POST':
		form = request.form.to_dict()
		# Check if the password and password1 actualy match
		if form['user_password'] == form['user_password1']:
			# If so try to find the user in db
			user = users_collection.find_one({"username" : form['username']})
			
			if user:
				flash("{form['username']} already exists!")
				return redirect(url_for('register'))

			# If user does not exist register new user
			else:
				# Hash password
				hash_pass = generate_password_hash(form['user_password'])
				#Create new user with hashed password
				users_collection.insert_one(
					{
						'username': form['username'],
						'password': hash_pass
						}
				)

				# Check if user is saved
				user_in_db = users_collection.find_one({"username": form['username']})

				if user_in_db:
					# Log user in (add to session)
					session['user'] = user_in_db['username']
					return redirect(url_for('profile', user=user_in_db['username']))

				else:
					flash("There was a problem saving your profile")
					return redirect(url_for('register'))
					
		else:
			flash("Passwords dont match!")
			return redirect(url_for('register'))

	return render_template("register.html")



# Log out

@app.route('/logout')

def logout():
	# Clear the session
	session.clear()
	flash('You were logged out!')
	return redirect(url_for('index'))



# Profile Page

@app.route('/profile/<user>')
def profile(user):
	# Check if user is logged in
	if 'user' in session:
		# If so get the user and pass him to template for now
		user_in_db = users_collection.find_one({"username": user})
		return render_template('profile.html', user=user_in_db)

	else:
		flash("You must be logged in!")
		return redirect(url_for('index'))













	



 
    
"""routes for other pages set up - functionality to be included later"""

@app.route("/addrecipe")
def addrecipe():
    return render_template("addrecipe.html")

@app.route("/allrecipeslist")
def allrecipeslist():
    return render_template("allrecipeslist.html")
    

@app.route("/recipesearch")
def recipesearch():
    return render_template("recipesearch.html")    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)