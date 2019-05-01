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

HTML 

(https://developer.mozilla.org/en-US/docs/Learn/HTML)
Hypertext markup language is used to create the structure of web pages.  It consists of tags which tell the browser
how to set out text and images on the page.  Hypertext is the method by which you move around on the web, markups are the tags
which set out the structure of the webpage, thus HTML is a language for web creation with its own structure and syntax.  The data 
in the tags is read by the web browser enabling you to create any web page you like.  In this project my templates are all written
in HTML.  There is a template for adding, deleting, editing and adding recipes as well as one for viewing information about
each island.  The base template sets out the way in which
the website should look and information from this is used in each of the other templates.

CSS

(https://developer.mozilla.org/en-US/docs/Learn/CSS/Introduction_to_CSS)
CSS stands for Cascading Style sheets which is a type of style language which sets out how the webpage should be styled.  It allows
the user to style the webpage in a particular way, making the UX richer and more meaningful for the user.

Bootstrap

(https://getbootstrap.com/)
Bootstrap is a popular framework for developing responsive websites.  It has built in classes which allow websites to be
responsive when viewed on any device.

Materializecss.com

(https://materializecss.com/)
Naterializecss.com is a modern responsive framework developed by google.  It has built in classes which allow websites to
be responsive when viewed on any device.  It also has many components which enhance the appearance of a webpage, e.g. forms, icons,
badges, buttons.  All these save the user time when desigining a website and enhance the UX.  It is also designed to speed up
development time and is easy to use.  I used version 0.100.2 - the most stable version as advised by CI.

Flask

(flask.pocoo.org/)
Flask is a microframework written in python.  Flask is therefore the "glue" that holds an application together.  Different types 
of file can co-exist in a flask application, with the base template holding the HTML base code for other templates.  In addition
flask provides security throught the wekzeug add in and the jinja templating language can also be used for markup on web pages.  

JQuery

(https://jquery.com/)

The project uses JQuery to simplify DOM manipulation.  Jquery is a javascript library that is used to provide interactivity
on websites.  The $ sign signals to the browser that jquery is being used.

Python

(https://www.python.org/)
I used Python version 3.7 to run my app.  Python is a high level programming language used for apps in many frameworks such as 
flask, pyramid and django.  Python supports many programming paradigms and is object orientated and has a comprehensive set of libraries.
Python is managed by a non profit organsation the Python software foundation.

Mongodb

(https://mlab.com/)
I used mongodb for my database.  Through pymongo (a module in python) I was able to connect my database to my flask app through the
use of appropriate environment variables.  Mongodb is a document database that provides the user with the facility to create,
read, update and delete documents in a database.  Mongodb documents are stored in  collections in json or bson format and this makes it easy to 
work with in Python and other programming languages.

Heroku 

(https://www.heroku.com/)
Heroku is a cloud platform that allows a developer to build, deliver, scale and monitor apps.  Heroku makes the experience of
deploying an app relatively straightforward.  

Chrome Developer Tools
I used chrome developer tools to work on my code.  Chrome dev tools are a set of tools designed to give the developer tools
to amend code in a testing environment in order to enhance the UX and functionality experience. 


Testing
--------
Testing was carried out by human beings.  The food Tech teacher at my school tested the app with her caribbean recipes and
students were able to add and delete their own recipes to the app.

Manual Testing
Add Recipe Page:

Go to the "Add Recipe" page.
Try to submit the empty form and verify that the recipe will not submit without a RECIPE NAME.
Try to submit the form without description and verify that the recipe will not submit without a RECIPE DESCRIPTION.
Try to submit the form without Vegan selected and verify that an error message appears.
My Recipes Page

Go to the "My Recipes" page.
Try to Delete a recipe and verify that an error message appears stating that if the user goes ahead the recipe will be permanently deleted.
My Dashboard

Once logged in, go to the Dashboard page.
Verify that the "Recipe Count" box is displaying the correct number of recipes.
Verify that the 3 graphs for "Base Ingredient", "Meal Type" & "Flavour" are displaying correctly.
Ratings

The Average Rating field does not update correctly
Edit A Recipe

when editing a recipe a new recipe will create instead of modifying the existing file.
Responsive Testing
The app was tested on Samsung S8, Apple iPhone 6, Apple iPad Air 2 and also using the Google Chrome inspect feature to test for repsonsiveness and any errors that occurred. The main issue which was found was the sidevar/ navbar not resizing.



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
----------

The following section describes the process to deploy this project to Heroku.

Ensure all required technologies are installed locally, as per the requirements.txtfile.
Via Linux Terminal, login to Heroku, using 'heroku login' command. Input Heroku login details.
Create new Heroku app, using 'heroku apps:create appname' command.
Push project to Heroku, using 'push -u heroku master' command.
Create scale, using 'heroku ps:scale web=1' command.
Login to Heroku and select newly created app.
Select settings. Select ‘Reveal Config'. Add IP 0.0.0.0 and PORT 5000.
From 'More' menu on the top right, select 'Restart all dynos'.
View app: In settings, select Domain URL, NOT Git URL to view your hosted application.
Deployed via Heroku: 

Credits
-------
Content
The text for the islands was copied from wikpaedia.

Media
The photos used in this site were obtained from pixabay and pixels.

Acknowledgements
I received inspiration for this project from my mentor Simen Daehlin, fellow students especially Jo Wings,
Miro, John Lynch and John L3.  Family, friends and my teaching colleagues and school students were also very helpful,

