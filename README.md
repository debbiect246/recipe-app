# CARIBBEAN RECIPE APP

In this project, I designed a recipe app for users to add, update, or search for caribbean recipes.
My late father was from the Caribbean island of Grenada and I was lucky enough to enjoy many family
holidays on the island in my childhood and later on as an adult with my own children.  I loved the
exotic fresh fruit and vegetables which were cheap and plentiful, sometimes free!  I loved the recipes that 
could be created with these wonderful ingredients.

I thought that it would be a good idea to bring produce an app to store details of user's favourite recipes
and it will also be a good place for users to search for other recipes.  Recipes can be categorised
into lunch and dinner recipes and users can search for recipes by type of recipe, recipe contents, island recipe comes from
and recipes which do not contain allergens.  The site also gives brief information on the island the recipe comes
from maybe encouraging a user to consider a visit to one of these lovely islands.

The app was deployed to heroku and can be accessed by clicking on this link 

https://recipe-app-flask-mongo.herokuapp.com/

## UX


### User stories

1.	 Each user has a unique username chosen by them and can only add and update their own recipes.
2.	 User can see each recipe on a recipe card. 
3.   User can catsearch for different types of recipes:  lunch, dinner and deserts.
4.	 User can also search for recipes which contain meat, fish, vegetables or fruit.
5.	 User can search for recipes which contain meat, fish, vegetables or sugar.
6.	 User can search for recipes which are free of a specified allergen.
7.	 User can add a recipe to the database.
8.	 User can  edit any of their recipes from the database.
9.	 Each recipe has a recipe view page which shows a picture, recipe ingredients and method, number of servings, allergens, recipe author, country of origin of the recipe.


## Wireframes

Wireframes were an integral part of the development process.  I designed these at the start of the project but as time went by they needed
several revisions.  Click on the link [wireframe](/recipe-app/UX/wireframe for caribbean recipe app) to see the final versions of my wireframes are shown below.


## Features

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

	 
## Additional features 


In the future I can add statistical pages showing ratings for each recipe, so that a 
user can see statistics on the nutritional ratings for each recipe and the ratings
for ease of use for each recipe.


## Features Left to Implement


1. Authenticated user login.  Users identities could be che

2.  Statistics on ratings for each recipe.

3.  Bar charts showing the number of calories in each recipe.

## Another feature idea

I would have liked to have added a delete button so that users can delete their 
recipes and store them in an archive, having "archived recipes" in my navbar.  At 
the moment I don't have the skills to do this but in the future when I have more time
I could add a new collection to store a set of archived recipes and add a route so
that a user could then add recipes to the archive.  This archive could then be searchable
by date and type of recipe, etc.


## Technologies Used


* HTML 

[HTML](https://developer.mozilla.org/en-US/docs/Learn/HTML)
Hypertext markup language is used to create the structure of web pages.  It consists of tags which tell the browser
how to set out text and images on the page.  Hypertext is the method by which you move around on the web, markups are the tags
which set out the structure of the webpage, thus HTML is a language for web creation with its own structure and syntax.  The data 
in the tags is read by the web browser enabling you to create any web page you like.  In this project my templates are all written
in HTML.  There is a template for adding, deleting, editing and adding recipes as well as one for viewing information about
each island.  The base template sets out the way in which
the website should look and information from this is used in each of the other templates.

* CSS

[CSS](https://developer.mozilla.org/en-US/docs/Learn/CSS/Introduction_to_CSS)
CSS stands for Cascading Style sheets which is a type of style language which sets out how the webpage should be styled.  It allows
the user to style the webpage in a particular way, making the UX richer and more meaningful for the user.


* Materializecss

[Materialisecss](https://materializecss.com/)
Naterializecss is a modern responsive framework developed by google.  It has built in classes which allow websites to
be responsive when viewed on any device.  It also has many components which enhance the appearance of a webpage, e.g. forms, icons,
badges, buttons.  All these save the user time when desigining a website and enhance the UX.  It is also designed to speed up
development time and is easy to use.  I used version 0.100.2 - the most stable version as advised by CI.

* Flask

[Flask](flask.pocoo.org/)
Flask is a microframework written in python.  Flask is therefore the "glue" that holds an application together.  Different types 
of file can co-exist in a flask application, with the base template holding the HTML base code for other templates.  In addition
flask provides security throught the wekzeug add in and the jinja templating language can also be used for markup on web pages.  

* JQuery

[jquery](https://jquery.com/)

The project uses JQuery to simplify DOM manipulation.  Jquery is a javascript library that is used to provide interactivity
on websites.  The $ sign signals to the browser that jquery is being used.

* Python

[python](https://www.python.org/)
I used Python version 3.7 to run my app.  Python is a high level programming language used for apps in many frameworks such as 
flask, pyramid and django.  Python supports many programming paradigms and is object orientated and has a comprehensive set of libraries.
Python is managed by a non profit organsation the Python software foundation.

Mongodb

[mongodb](https://mlab.com/)
I used mongodb for my database.  Through pymongo (a module in python) I was able to connect my database to my flask app through the
use of appropriate environment variables.  Mongodb is a document database that provides the user with the facility to create,
read, update and delete documents in a database.  Mongodb documents are stored in  collections in json or bson format and this makes it easy to 
work with in Python and other programming languages.

* Heroku 

[heroku](https://www.heroku.com/)
Heroku is a cloud platform that allows a developer to build, deliver, scale and monitor apps.  Heroku makes the experience of
deploying an app relatively straightforward.  

* Chrome Developer Tools
I used chrome developer tools to work on my code.  Chrome dev tools are a set of tools designed to give the developer tools
to amend code in a testing environment in order to enhance the UX and functionality experience. 


## Testing

Testing was carried out by human beings.  The food Tech teacher at my school tested the app with her caribbean recipes and
students were able to add and delete their own recipes to the app.

### Manual Testing

* Log in page:

  Ensure that only registered users can login.  If an unregistered user tries to log in they are directed to the 
register page.

* All recipes list page:

Click on All Recipes item in the menu and ensure that all recipes are shown.
The name of the recipe, recommended type of recipe, recipe ingredients and allergens are shown on the front of 
the card for each recipe.  Clicking on the three vertical dots on the right hand side of the card shows the steps
involved in making the recipe.
There is a link at the bottom of the reverse card which when clicked shows information about the recipe island
together with a map of the caribbean.


* Add Recipe Page:

Go to the "Add Recipe" page.
Try to submit the empty form and verify that the recipe will not submit without a RECIPE NAME.
Try to submit the form without description and verify that the recipe will not submit without a RECIPE DESCRIPTION.
Try to submit the form without Vegan selected and verify that an error message appears.
My Recipes Page

* Using the "Edit Recipe" button.

Try to edit a recipe and verify that a user can only edit a recipe if they are the author of the recipe.
Input fields are present for each recipe.  User can type into these or use drop down items to make selections.
Once a recipe has been edited the allrecipes list page renders and users can see that the recipe has been edited.

* Find Recipe page

Try to find a recipe by recipe type - lunch, dinner or dessert.
Try to find a recipe by the main type of ingredient it contains - meat, fish, vegetables or sugar.
Try to find a recipe which comes from a particular caribbean island.
Try to find a recipe which does not contain a user specified allergen.
For each of the searches above a results page should show recipes which match the user specified
criteria.

* Add Recipe page

Try to add a recipe by clicking on add recipe item in menu.
List of fields should appear and user can type recipe details into each field.
Some fields have drop down menus so that user can select correct item to input into field thus
eliminating the possibility of making mistakes when entering the recipe details in these fields.

* Add recipe page:

Go to the "Add recipe" page
Type in details of recipe.
Check that recipe appears in databases and that a new card has been created for it with details entered.
Note that user does not need to enter all recipe details as recipe can later be edited by user who created it.

The app was tested on Samsung S8, Apple iPhone 6, Apple iPad Air 2 and also using the Google Chrome inspect feature to test for repsonsiveness and any errors that occurred. The main issue which was found was the sidevar/ navbar not resizing.


## Interesting bugs or problems I discovered during testing

The most annoying bug I came across was when I was trying to push my code to heroku.  I followed
the instructions above but got an error 500 after each attempt.  Despite looking at my code in detail I couldnt find
anything wrong with it.  My mentor looked at my code later and pointed out that the number in the uri was incoffect so 
when pushing to Heroku I got an authentication error.  Once I put in the corect number in my uri (which I cout from mlab), 
I was able to successfully push my code to heroku.


## Development process of my project

* I created a new workspace in my cloud9 account and chose a blank template.
* I then imported flask using the terminal.  `sudo pip3 install flask`
* I created a static folder for my images and my styles.css files and a templates folder for my templates.
* Next thing was to set up my base template html file and my app.py file. 
* In my base html file I started with html boiler plate then added in the following command '{% block content %} {% endblock %}' so 
  that my nav bar would appear on each page.  I created my nav bar using an ordered list.  Effects for the nav bar were put into my
  styles.css file.
* In my app.py file I imported all the modules I would need and then set up a secret key and set my debug to True so that I could get
  an error log if there was something wrong with my code I could sort it out with the help of the error log.  I also set up my secret 
  key as part of my cookie encryption.
* At this point I pushed my app to heroku in readiness for the final push to heroku later on.  This meant I had to create my procifle 
  and requirements file in order for the app to run.
* I created my database in mlab.  This consisted of 3 collections:  1 for my recipes, 1 for the Caribbean islands and 1 for my users.
  The recipe collection was used to hold details of all my recipes.  My caribbean island collection held the details of 21 Caribbean islands.
  My user collection held the names and passwords of all users of the recipe app.  It was used to endure that only recipe authors
  could edit their own recipes and also enabled users to login to the app.
* I entered 8 recipes into my recipe collection,which consisted of 15 key values in json format.
* I returned to my app.py page to connect my database to my app.  I entered the environment details in to my config.py file and
  then put this in gitignore.
* I then built my allrecipeslist page so that my recipes would display on the screen.  Initially I used accordian format from 
  materializecss but then changed the display to cards on the advice of my mentor.  I checked that the allrecipeslist page worked,
  and that summary information was displayed on the front of the card with a picture of the recipe, and on clicking on the three dot icon
  on the right hand top side of the card, the flip side of the card would then be shown together with the ingredients and method for
  making the recipe.
* I then put together my addrecipes and editrecipes pages using addrecipes page as a template for my editrecipes page.
* I checked that both my addrecipes and editrecipes pages worked ensuring that a user could add a recipe and only the author of the recipe
  could edit a recipe.
* I returned to my allrecipeslist page and put in a link to my islands collections so that users could find out more about
  the island a recipe came from.  This involved building an island page which displayed a picture of the island, a picture of the map of
  the caribbean and some information about the island.  Users checked that this worked.
* Finally I build my findrecipe page.  This enabled a user to find a recipe which was either a lunch, dinner or dessert recipe, or to find a recipe which 
  contained meat, fish, vegetables or sugar.  Users could also search for recipes which came from speificifed islands, or search for 
  recipes which did not contain specified allergens.  As part of this I created a results page which displayed the results of each
  search.
* I then  created a login and register page.  The login page allowed registered users to access the app, and if a user was not registered, then
  the register page enabled them to register.
* Lastly I checked that the entire app worked before doing a final push to heroku, making sure that my environment variables were correctly
  input into the heroku dashboard for the app.



## Deployment

The following section describes the process to deploy this project to Heroku.

* Ensure all required technologies are installed locally, as per the requirements.txtfile.
* Via Linux Terminal, login to Heroku, using 'heroku login' command. Input Heroku login details.
* Create new Heroku app, using 'heroku apps:create appname' command.
* Push project to Heroku, using 'push -u heroku master' command.
* Create scale, using 'heroku ps:scale web=1' command.
* Login to Heroku and select newly created app.
* Select settings. Select ‘Reveal Config'. Add IP 0.0.0.0 and PORT 5000.
* From 'More' menu on the top right, select 'Restart all dynos'.
* View app: In settings, select Domain URL, NOT Git URL to view your hosted application.
* App was now deployed via Heroku

## Credits

Content
The text for the islands was copied from wikpaedia.

Media
The photos used in this site were obtained from pixabay and pixels.

Acknowledgements
I received inspiration for this project from my mentor Simen Daehlin, fellow students especially Jo Wings,
Miro, John Lynch and John Longatty.  Family, friends and my teaching colleagues and school students were also very helpful 
in giving me feedback.  I used pymongo documentation to help me get my code correct.


