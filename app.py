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


#route for home page
@app.route("/")
def index():
    """Main page"""
    return render_template("index.html")
    

#route for eventual log in page
    
@app.route("/", methods = ["POST"])
def login():
    session["username"]=request.form["username"]
    return redirect(url_for("user",username=session["username"]))
    
@app.route("/<username>")
def user(username):
    """Display welcome message"""
    return "<h1>Welcome {0}</h1>".format(username)
 
#route to display all recipes in summary and expanded form with accordion dropdown

@app.route('/allrecipeslist')
def allrecipeslist():
    recipes = mongo.db.recipes.find()
    return render_template('allrecipeslist.html', recipes=recipes)

#route to display recipe island - user clicks on this from all recipes page

@app.route('/islands/<recipe_island>', methods=["GET","POST"])
def islands(recipe_island):
    print(recipe_island)
    this_island= mongo.db.islands.find_one({'recipe_island':recipe_island})
    return render_template('islands.html', this_island=this_island)

#route for page where user can add a recipe    
 
@app.route("/addrecipe")
def addrecipe():
    recipes = mongo.db.recipes.find()
    return render_template("addrecipe.html", recipes=recipes) 
    
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('allrecipeslist'))

#route for edit recipe page

@app.route("/editrecipe/<recipe_id>")
def editrecipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('editrecipe.html', recipe=the_recipe)

@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_name':request.form.get('recipe_name'),
        'recipe_island':request.form.get('recipe_island'),
        'recipe_intro': request.form.get('recipe_intro'),
        'recipe_ingredients': request.form.get('recipe_ingredients'),
        'recipe_picture':request.form.get('recipe_picture'),
        'method':request.form.get('method'),
        'allergens':request.form.get('allergens'),
        'recipe_author':request.form.get('recipe_author'),
        'recipe_contains':request.form.get('recipe_contains'),
        'nutritional_info' : {
        'number_servings':request.form.get('nutritional_info.number_servings'),
        'calories_per_serve':request.form.get('nutritional_info.calories_per_serve'),
        'protein_grammes_per_serve':request.form.get('nutritional_info.protein_grammes_per_serve'),
        'fat_grammes_per_serve':request.form.get('nutritional_info.fat_grammes_per_serve'),
        'fibre_grammes_per_serve':request.form.get('nutritional_info.fibre_grammes_per_serve'),
        'carb_grammes_per_serve':request.form.get('nutritional_info.carb_grammes_per_serve'),
        }

    })
    return redirect(url_for('allrecipeslist'))
 
#route for delete recipe page - user access this from all recipes list page  
    
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('allrecipeslist'))

#route for find recipe page - user can search for lunch, dinner, dessert recipes, allergens, recipes from specified islands. 

@app.route("/findrecipe", methods=['GET', 'POST'])
def findrecipe():
    recipes=mongo.db.recipes
    if request.method == 'POST':
        requested_type = request.form.get("recipe_type")
        print(requested_type)
        recipes = mongo.db.recipes.find({"recipe_type": requested_type})
        return render_template("results.html", recipes=recipes)
        
    return render_template("findrecipe.html")

@app.route("/findrecipecontents", methods=['GET', 'POST'])   
def findrecipecontents():
    recipes=mongo.db.recipes
    if request.method == 'POST':
        requested_contents = request.form.get("recipe_contains")
        print(requested_contents)
        recipes = mongo.db.recipes.find({"recipe_contains": requested_contents})
        return render_template("results.html", recipes=recipes)
        
    return render_template("findrecipe.html")
    
@app.route("/findrecipeisland", methods=['GET', 'POST'])   
def findrecipeisland():
    recipes=mongo.db.recipes
    if request.method == 'POST':
        requested_island = request.form.get("recipe_island")
        print(requested_island)
        recipes = mongo.db.recipes.find({"recipe_island": requested_island})
        return render_template("results.html", recipes=recipes)
        
    return render_template("findrecipe.html")    
    

#route for page to display results of searches
		
@app.route("/results")
def displayresults():
    return render_template('results.html')	
    
#route for eventual log out page
    
@app.route('/log_out')
def log_out():
    if session:
        session.clear()
        return render_template("logout.html")
    else:
        return redirect(url_for("index"))

# instructions to run app
 
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)