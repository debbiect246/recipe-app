import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
from config import dbconfig


app = Flask(__name__)
app.secret_key = "randomstring123"

app.config["MONGO_DBNAME"] = 'recipe_manager'
app.config["MONGO_URI"] = dbconfig()

mongo = PyMongo(app)

"""Home page with login form"""

@app.route("/")
def index():
    """Main page"""
    return render_template("login.html", register=mongo.db.register.find())


@app.route('/')
def get_recipes():
    return render_template("allrecipeslist.html", recipes=mongo.db.recipes.find())

""" Register form - this uses the POST method, insert user into database using details
given by user (username and password), then once this is done, redirect user to allrecipeslist
page"""

@app.route('register',methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        register=mongo.db.register
        reg_id = register.insert_one(request.form.to.dict())
        object_id = reg_id.inserted_id
        return redirect(url_for('allrecipeslist', register_id=object_id))
    return render_template('register.html')
        

""" Login page action.  This uses the post method and will find the user name and password in the
register collection in mongo db.  If it matches then user is redirected to allrecipeslist page.  If 
it doesnt match then user is told that password is incorrect and is asked to login again. """

@app.route('/login', methods=["GET","POST"])
def login():
    if request.method =='POST':
        login_user = mongo.db.register.find_one({'username': request.form['username']})
        form = request.form
        if login_user:   #if user login and password are ok display the allrecipeslist page
            if (form["password"] == login_user["password"]):   
                session['username'] = login_user["username"]
                return redirect(url_for('allrecipeslist', register_id = login_user["_id"]))
           
            else:  #if user password is not correct
                flash("Incorrect  password")
            
        else:   #if user does not exist
            flash("User does not exist")
            return redirect(url_for('register'))
    return render_template('login.html')
                
        



@app.route("/", methods = ["POST"])
def login():
    session["username"]=request.form["username"]
    return redirect(url_for("user",username=session["username"]))
    
@app.route("/<username>")
def user(username):
    return "<h1>Welcome {0}</h1>".format(username)

"""

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