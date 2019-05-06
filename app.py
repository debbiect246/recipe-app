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


#Home page with login form

@app.route('/')
def index():
    return render_template('login.html', register=mongo.db.register.find_one())

"""Register form action  method must be post.  Insert  new user in database using form on login page, then redirect user to allrecipeslist page.
"""

@app.route('/register',methods=['POST','GET'])
def register():
    if request.method == 'POST':
        register = mongo.db.register
        reg_id = register.insert_one(request.form.to_dict())
        # print(register)
        object_id = reg_id.inserted_id
        return redirect(url_for('allrecipeslist',register_id=object_id))
    return render_template('register.html')

"""
Login page action. Method must be post - find the given password and username and  if it matches then
redirect to allrecipeslist but ifnot redirect to register and if password only incorrect flash message to show that  password is incorrect
"""
@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == 'POST':
        login_user = mongo.db.register.find_one({'username': request.form['username']})
        form = request.form
        if login_user:
            if(form["password"] == login_user["password"]): # if password correct
                session['username'] = login_user["username"]
                return redirect(url_for('allrecipeslist',register_id = login_user["_id"]))
            else: # and if password is not correct
               flash("Incorrect password") 
        else:# if not exist
            flash("User does not exist")
            return redirect(url_for('register'))
    return render_template('login.html')
            
 
#route to display all recipes in summary and expanded form with cards

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

@app.route("/editrecipe/<recipe_id>/<username>")
def editrecipe(recipe_id, username):
    the_user = mongo.db.register.find_one({"username": username})
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('editrecipe.html', recipe=the_recipe, register=the_user)
    
    
@app.route('/update_recipe/<recipe_id> ', methods=["POST"])
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
        'number_servings':request.form.get('number_servings'),
        'calories_per_serve':request.form.get('calories_per_serve'),
        'protein_grammes_per_serve':request.form.get('protein_grammes_per_serve'),
        'fat_grammes_per_serve':request.form.get('fat_grammes_per_serve'),
        'fibre_grammes_per_serve':request.form.get('fibre_grammes_per_serve'),
        'carb_grammes_per_serve':request.form.get('carb_grammes_per_serve'),
        })

   
    return redirect(url_for('allrecipeslist'))
 
#route for delete recipe function - user access this from all recipes list page  
    
@app.route("/delete_recipe/<recipe_id>/<username>")
def delete_recipe(recipe_id, username):
    the_user = mongo.db.register.find_one({"username": username})
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('deleterecipe', recipe=the_recipe, register=the_user))

#routes for find recipe page - user can search for lunch, dinner, dessert recipes, allergens, recipes from specified islands. 
#code for searching for lunch, dinner or dessert recipes

@app.route("/findrecipe", methods=['GET', 'POST'])
def findrecipe():
    recipes=mongo.db.recipes
    if request.method == 'POST':
        requested_type = request.form.get("recipe_type")
        
        recipes = mongo.db.recipes.find({"recipe_type": requested_type})
        return render_template("results.html", recipes=recipes)
        
    return render_template("findrecipe.html")
    
#code for searching for recipes which contain meat, vegetables, fish or sugar as the main ingredient.

@app.route("/findrecipecontents", methods=['GET', 'POST'])   
def findrecipecontents():
    recipes=mongo.db.recipes
    if request.method == 'POST':
        requested_contents = request.form.get("recipe_contains")
        
        recipes = mongo.db.recipes.find({"recipe_contains": requested_contents})
        return render_template("results.html", recipes=recipes)
        
    return render_template("findrecipe.html")
    
#code for searching for recipes which come from particular islands.
    
@app.route("/findrecipeisland", methods=['GET', 'POST'])   
def findrecipeisland():
    recipes=mongo.db.recipes
    if request.method == 'POST':
        requested_island = request.form.get("recipe_island")
        
        recipes = mongo.db.recipes.find({"recipe_island": requested_island})
        return render_template("results.html", recipes=recipes)
        
    return render_template("findrecipe.html")  
    
#code for searching for recipes which do not contain specified allergens.

@app.route("/findallergensfree", methods=['GET', 'POST'])   
def findallergensfree():
    recipes=mongo.db.recipes
    if request.method == 'POST':
        requested_allergen = request.form.get("allergens")
        recipes = mongo.db.recipes.find({"allergens": {"$ne: requested_allergen"}})
        return render_template("results.html", recipes=recipes)
        
    return render_template("findrecipe.html")  

    

#route for page to display results of searches
		
@app.route("/results")
def displayresults():
    return render_template('results.html')	
    
#route for log out page
    
@app.route('/log_out')
def log_out():
    return render_template('login.html')

# instructions to run app
 
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)