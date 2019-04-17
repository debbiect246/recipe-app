CARIBBEAN RECIPE APP
---------------------
In this project, I designed a recipe app for users to add, update, or search for caribbean recipes.
My late father was from the Caribbean island of Grenada and I was lucky enough to enjoy many family
holidays on the island in my childhood and later on as an adult with my own family.  I loved the
fresh fruit and vegetables which were cheap and plentiful, sometimes free!  I loved the recipes that 
could be created with these wonderful ingredients.

I thought that it would be a good idea to bring produce an app to store details of user' favourite recipes
and it will also be a good place for users to search for other recipes.  Recipes can be categorised
into lunch and dinner recipes and users can search for recipes by type of recipe, recipe contents, island recipe comes from
and recipes which do not contain allergens.


UX
--

User stories
------------
1.	 Each user has a unique username chosen by them and can only add, review, delete and update their own recipes.
2.	 User can choose a recipe from the database and see a summary view of it. 
3.   User can catsearch for different types of recipes:  lunch, dinner and deserts.
4.	 User can also search for recipes which contain meat, fish, vegetables or fruit.
5.	 User can add a recipe to the database.
6.	 User can  edit or delete any of their recipes from the database.
7.	 Each recipe has a recipe view page which shows a picture, recipe ingredients and method, number of servings, allergens, recipe author, country of origin of the recipe.
8.	 User can see statistics on the nutritional ratings for each recipe.
9.	 User can see statistics on ratings for each recipe.

Wireframes are shown in my UX folder.


Features
--------
The features I implemented successfully are shown below:

1.	 Each user has a unique username chosen by them and can only add, delete and update their own recipes.  
    Achieved through use of login page.  Users are stored in a collection in the database- they are authenticated against
    this when they log in.  The author of the recipe is stored in the database and only the authenticated user can 
    edit and delete their own recipes.  All users can see all recipes and add a recipe to the database.

2.	 User can choose a recipe from the database and see a summary view of it. 
	 Each recipe is displayed on a recipe card.
     The recipe card shows a picture of the recipe, displays nutritional information about the recipe and  has a list of
     allergens at the top of the card.  A user can click on the vertical link on the top right of each card to get a 
     list of ingredients for each recipe and a list of steps for successfully making the recipe.
    
3.	User can choose from 3 main categories of recipes:  lunch, dinner and deserts.
    Each user is able to do a search for lunch, dinner and dessert recipes.  The recipe card shown as a result of this search
    will show a picture of the finished recipe together with nutritional and allergen information.  Clicking on the vertical link
    on the top right of the card brings up the ingredients needed and instructions for making the recipe.

4.	User can also choose from vegetarian, meat based, vegetable and fruit recipes.
    Each user is able to do a search for meat based, fish based, vegetable based or fruit based recipes. The recipe card shown as
    a result of this search will show a picture of the finished recipe together with nutritional and allergen information. 
    Clicking on the vertical link  on the top right of the card brings up the ingredients needed and instructions for making 
    the recipe.

5.  User can also search for a recipe by island.
    All users can search for recipes which come from a particular carribean island. There are 21 islands in the islands collection
    of the database so there is quite a choice.  In addition if a user needs more information on a caribbean island they can 
    click on the link at the bottom of the relevant recipe card and a brief summary of the island will appear, showing a picture
    of the island, information on the island population, the geographical location of the island and the main languages spoken 
    on the island.

6.  Users can search for a recipe which does not contain specified allergens.
    All users can search for recipes which do not contain allergens specified by the user, and there is also an option for
    users to find recipes which do not contain any allergens.
	
7.	 User can add a recipe to the database. 
    All registered users can add a recipe to the database.  If a user does not have an account they can create one at the
    start of the app - once they have an account they are free to add recipes to the database.
	 
Additional features 
-------------------

In the future I can add statistical pages showing ratings for each recipe.

Features Left to Implement

Statistics on ratings for each recipe.
Bar charts showing the number of calories in each recipe.

Another feature idea

Technologies Used
-----------------
HTML: 
HTML - hypertext markup language is used to create the structure of web pages.  It consists of tags which tell the browser
how to set out text and images on the page.  Hypertext is the method by which you move around on the web, markups are the tags
which set out the structure of the webpage, thus HTML is a language for web creation with its own structure and syntax.  The data 
in the tags is read by the web browser enabling you to create any web page you like.  In this project my templates are all written
in HTML.  There is a template for adding, deleting, editing and adding recipes as well as one for viewing information about
each island.  The base template sets out the way in which
the website should look and information from this is used in each of the other templates.

CSS:
CSS stands for Cascading Style sheets which is a type of style language which sets out how the webpage should be styled.  It allows
the user to style the webpage in a particular way, making the UX richer and more meaningful for the user.

Bootstrap:
Bootstrap is a popular framework for developing responsive websites.  It has built in classes which allow websites to be
responsive when viewed on any device.

Materializecss.com:
Naterializecss.com is a modern responsive framework developed by google.  It has built in classes which allow websites to
be responsive when viewed on any device.  It also has many components which enhance the appearance of a webpage, e.g. forms, icons,
badges, buttons.  All these save the user time when desigining a website and enhance the UX.  It is also designed to speed up
development time and is easy to use.  I used version 0.100.2 - the most stable version as advised by CI.

Flask:
Flask is a microframework written in python.  Flask is therefore the "glue" that holds an application together.  Different types 
of file can co-exist in a flask application, with the base template holding the HTML base code for other templates.  In addition
flask provides security throught the wekzeug add in and the jinja templating language can also be used for markup on web pages.  

JQuery:
The project uses JQuery to simplify DOM manipulation.  Jquery is a javascript library that is used to provide interactivity
on websites.  The $ sign signals to the browser that jquery is being used.

Testing
--------
Testing was carried out by human beings.  The food Tech teacher at my school tested the app with her caribbean recipes and
students were able to add their own recipes to the app.


Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

Add recipe page:
Go to the "Add recipe" page
Type in details of recipe.
Check that recipe appears in databases and that a new card has been created for it with details entered.
Note that user does not need to enter all recipe details as recipe can later be edited by user who created it.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

Deployment
This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:

Different values for environment variables (Heroku Config Vars)?
Different configuration files?
Separate git branch?
In addition, if it is not obvious, you should also describe how to run your code locally.

Credits
Content
The text for section Y was copied from the Wikipedia article Z
Media
The photos used in this site were obtained from ...
Acknowledgements
I received inspiration for this project from X