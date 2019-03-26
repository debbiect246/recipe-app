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


@app.route("/")
def index():
    """Main page"""
    return render_template("index.html")
    
@app.route("/", methods = ["POST"])
def login():
    session["username"]=request.form["username"]
    return redirect(url_for("user",username=session["username"]))
    
@app.route("/<username>")
def user(username):
    """Display welcome message"""
    return "<h1>Welcome {0}</h1>".format(username)
 

@app.route('/allrecipeslist')
def allrecipeslist():
    recipes = mongo.db.recipes.find()
    return render_template('allrecipeslist.html', recipes=recipes)
 
@app.route("/addrecipe")
def addrecipe():
    return render_template("addrecipe.html")   
  
@app.route("/recipesearch")
def recipesearch():
    return render_template("recipesearch.html") 
    
@app.route("/editrecipe")
def editrecipe():
    return render_template("editrecipe.html")
    
@app.route("/deleterecipe")
def deleterecipe():
    return render_template("deleterecipe.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)