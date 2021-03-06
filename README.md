# [CARIBBEAN RECIPE APP](https://recipe-app-flask-mongo.herokuapp.com/)

In this project, I designed a recipe app for users to add, update, or search for caribbean recipes.
My late father was from the Caribbean island of Grenada and I was lucky enough to enjoy many family
holidays on the island in my childhood and later on as an adult with my own children.  I loved the
exotic fresh fruit and vegetables which were cheap and plentiful, sometimes free and I loved the recipes that 
could be created with these wonderful ingredients.

I wanted to produce an app to store details of user's favourite recipes from the Caribbean, and to make these searchable
by main ingredient, recipe island and allergen as well as having links to information about different caribbean islands.
I| decided to categorise these recipes into lunch and dinner recipes nd list the main ingredient of the recipe.
I hoped that by giving the user some basic information on each caribbean island that a recipe came from that they
might be tempted to visit the particular island and enjoy some of the wonderful food there for themselves.

The app was deployed to heroku and can be accessed by clicking on the title above. 



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
several revisions.  Click on the link [wireframe](https://github.com/debbiect246/recipe-app/blob/master/UX/wireframe.pdf) to see the final versions of my wireframes.


## Features

The features I implemented successfully are shown below:

1.  Each user has a unique username chosen by them and can only add, delete and update their own recipes.  
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


1. Authenticated user login.  Users identities could be checked using two factor authentication. This could be implemented in 
   django or another python framework.

2.  Ensuring that duplicate recipes cannot be added to the database; an error message to flash up if a user attempts to add a 
    duplicate recipe - this would need for all 15 fields to be checked after recipe was submitted to see if any of the recipes
    in the database are an exact match for the recipe being entered. 

2.  Statistics on ratings for each recipe.  A ratings collection could be used for this. The ratings could be implemented using
    a number of technologies including crossfilter and matlab.

3.  Bar charts showing the number of calories in each recipe.  This could be implemented using d3 and crossfilter.

## Another feature idea

I would have liked to have added a delete button so that users can delete their 
recipes and store them in an archive, having "archived recipes" in my navbar.  At 
the moment I don't have the skills to do this but in the future when I have more time
I could add a new collection to store a set of archived recipes and add a route so
that a user could then add recipes to the archive.  This archive could then be searchable
by date and type of recipe, etc.


## Technologies Used


[HTML](https://developer.mozilla.org/en-US/docs/Learn/HTML)

Hypertext markup language is used to create the structure of web pages.  It consists of tags which tell the browser
how to set out text and images on the page.  Hypertext is the method by which you move around on the web, markups are the tags
which set out the structure of the webpage, thus HTML is a language for web creation with its own structure and syntax.  The data 
in the tags is read by the web browser enabling you to create any web page you like.  In this project my templates are all written
in HTML.  There is a template for adding, deleting, editing and adding recipes as well as one for viewing information about
each island.  The base template sets out the way in which
the website should look and information from this is used in each of the other templates.

[CSS](https://developer.mozilla.org/en-US/docs/Learn/CSS/Introduction_to_CSS)

stands for Cascading Style sheets which is a type of style language which sets out how the webpage should be styled.  It allows
the user to style the webpage in a particular way, making the UX richer and more meaningful for the user.


[Materialisecss](https://materializecss.com/)

is a modern responsive framework developed by google.  It has built in classes which allow websites to
be responsive when viewed on any device.  It also has many components which enhance the appearance of a webpage, e.g. forms, icons,
badges, buttons.  All these save the user time when desigining a website and enhance the UX.  It is also designed to speed up
development time and is easy to use.  I used version 0.100.2 - the most stable version as advised by CI.

[Flask](http://flask.pocoo.org/)

Flask is a microframework written in python.  Flask is therefore the "glue" that holds an application together.  Different types 
of file can co-exist in a flask application, with the base template holding the HTML base code for other templates.  In addition
flask provides security throught the wekzeug add in and the jinja templating language can also be used for markup on web pages. 

[Jinja2](http://jinja.pocoo.org/docs/2.10/)

Jinja 2 is a templating language which is used for rendering data in html templates and is used for communication between
the front end and back end of an app.
  

[jquery](https://jquery.com/)

jquery is used to simplify DOM manipulation.  Jquery is a javascript library that is used to provide interactivity
on websites.  The $ sign signals to the browser that jquery is being used.

[python](https://www.python.org/)

I used Python version 3.7 to run my app.  Python is a high level programming language used for apps in many frameworks such as 
flask, pyramid and django.  Python supports many programming paradigms and is object orientated and has a comprehensive set of libraries.
Python is managed by a non profit organsation the Python software foundation.

[mongodb](https://mlab.com/)

I used mongodb for my database.  Through pymongo (a module in python) I was able to connect my database to my flask app through the
use of appropriate environment variables.  Mongodb is a document database that provides the user with the facility to create,
read, update and delete documents in a database.  Mongodb documents are stored in  collections in json or bson format and this makes it easy to 
work with in Python and other programming languages.

[Heroku](https://en.wikipedia.org/wiki/Heroku)

Heroku is a cloud platform that allows a developer to build, deliver, scale and monitor apps.  Heroku makes the experience of
deploying an app relatively straightforward.  

[Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools/)

I used chrome developer tools to work on my code.  Chrome dev tools are a set of tools designed to give the developer tools
to amend code in a testing environment in order to enhance the UX and functionality experience.  I was also able to test the 
responsiveness of my app using these tools.


## Testing

Testing was carried out by human beings.  The food Tech teacher at my school tested the app with her caribbean recipes and
students were able to add and edit their own recipes.  Details of testing done by testers on a page by page basis is shown
below together with images of each page.  I also tested the app.

### Manual Testing

* Log in page:

  Ensure that only registered users can login.  If an unregistered user tries to log in they are directed to the 
register page.  

![login page](https://github.com/debbiect246/recipe-app/blob/master/static/images/imageofloginpage.jpg)


* All recipes list page:

Click on All Recipes item in the menu and ensure that all recipes are shown.
The name of the recipe, recommended type of recipe, recipe ingredients and allergens are shown on the front of 
the card for each recipe.  Clicking on the three vertical dots on the right hand side of the card shows the steps
involved in making the recipe.
There is a link at the bottom of the reverse card which when clicked shows information about the recipe island
together with a map of the caribbean.

![Recipe list page](https://github.com/debbiect246/recipe-app/blob/master/static/images/imageofallrecipespage.jpg)


* Add Recipe Page:

Go to the "Add Recipe" page.
Type in details of recipe.
Check that recipe appears in databases and that a new card has been created for it with details entered.
Note that user does not need to enter all recipe details as recipe can later be edited by user who created it.
Try to submit the empty form and verify that the recipe will not submit without a RECIPE NAME.
Try to submit the form without description and verify that the recipe will not submit without a RECIPE DESCRIPTION.
Try to submit the form without Vegan selected and verify that an error message appears.
Try to add a recipe by clicking on add recipe item in menu.
List of fields should appear and user can type recipe details into each field.
Some fields have drop down menus so that user can select correct item to input into field thus
eliminating the possibility of making mistakes when entering the recipe details in these fields.
Database administrator checks that recipe has been successfully added to the database.


![Recipe list page](https://github.com/debbiect246/recipe-app/blob/master/static/images/imageofaddrecipepage.jpg)


* Using the "Edit Recipe" button.

Try to edit a recipe and verify that a user can only edit a recipe if they are the author of the recipe.
Input fields are present for each recipe.  User can type into these or use drop down items to make selections.
Once a recipe has been edited the allrecipes list page renders and users can see that the recipe has been edited.

* Find Recipe page

Try to find a recipe by recipe type - lunch, dinner or dessert.
Try to find a recipe by the main type of ingredient it contains - meat, fish, vegetables or sugar.
Try to find a recipe which comes from a particular caribbean island.
Try to find a recipe which does not contain a user specified allergen.
For each of the searches above a results page should show recipes which match the user specified criteria with 
each recipe found being displayed on a separate card.  Page title should be "Recipes which match your criteria are shown below"

![Recipe list page](https://github.com/debbiect246/recipe-app/blob/master/static/images/imageoffindrecipepage.jpg)


* Island page

Click on link for find out more information about this island.
Check that page is rendered showing recipe island, map of caribbean island and information on size of recipe island,
location of recipe island, and languages spoken on recipe island, as well as a map of the caribbean at the bottom
of the page showing all caribbean islands.

![Recipe list page](https://github.com/debbiect246/recipe-app/blob/master/static/images/imageofislandpage.jpg)


The app was tested on Samsung S8, Apple iPhone 6, Apple iPad Air 2 and also using the Google Chrome inspect feature to test for repsonsiveness and any errors that occurred. The main issue which was found was the sidevar/ navbar not resizing.


## Interesting bugs or problems I discovered during testing

The most annoying bug I came across was when I was trying to push my code to heroku.  I followed
the instructions above but got an error 500 after each attempt.  Despite looking at my code in detail I couldnt find
anything wrong with it.  My mentor looked at my code later and pointed out that the number in the uri was incoffect so 
when pushing to Heroku I got an authentication error.  Once I put in the corect number in my uri (which I cout from mlab), 
I was able to successfully push my code to heroku.

After I pushed my app to heroku I needed to change some details and needed to remember to set debug back to true in the
cloud9 editor.  However on more than one occasion I forgot to change debug back to false resulting in error messages.

I also discovered that the cloud9 editor can be temperamental and had to log off and log back on several times on some 
occasions so that I could run my code.


## Development process of my project

1. I created a new workspace in my cloud9 account and chose a blank template.
2. I then imported flask using the terminal.  `sudo pip3 install flask`
3. I created a static folder for my images and my styles.css files and a templates folder for my templates.
4. Next thing was to set up my base template html file and my app.py file. 
5. In my base html file I started with html boiler plate then added in the following command '{% block content %} {% endblock %}' so 
  that my nav bar would appear on each page.  I created my nav bar using an ordered list.  Effects for the nav bar were put into my
  styles.css file.
6. In my app.py file I imported all the modules I would need and then set up a secret key and set my debug to True so that I could get
  an error log if there was something wrong with my code I could sort it out with the help of the error log.  I also set up my secret 
  key as part of my cookie encryption.
7. At this point I pushed my app to heroku in readiness for the final push to heroku later on.  This meant I had to create my procifle 
  and requirements file in order for the app to run.
8. I created my database in mlab.  This consisted of 3 collections:  1 for my recipes, 1 for the Caribbean islands and 1 for my users.
  The recipe collection was used to hold details of all my recipes.  My caribbean island collection held the details of 21 Caribbean islands.
  My user collection held the names and passwords of all users of the recipe app.  It was used to endure that only recipe authors
  could edit their own recipes and also enabled users to login to the app.
9. I created an admin user, creating a login and password in this format, noting this format as I would need it later to put in my
   config.py file  `mongodb://<dbuser>:<dbpassword>@XXXXXX.mlab.com:XXXXX/recipe_manager`
10. I entered 8 recipes into my recipe collection,which consisted of 15 key values in json format. 
    Schema for my recipe collection:
![recipe collection](https://github.com/debbiect246/recipe-app/blob/master/UX/recipeschema.jpg)
    I entered 21 caribbean islands into my islands collection - the schema for this is below.
    Schema for my islands collection:
![login page](https://github.com/debbiect246/recipe-app/blob/master/UX/islandsschema.jpg)
    Schema for my users collection is in json format as shown below.
    ``` {
    "_id": {
        "$oid": "5cb433bdfb6fc037f0791287"
    },
    "username": "debbie",
    "password": "debbie"
    }```


11. I returned to my app.py page to connect my database to my app.  I entered the environment details in to my config.py file and
    then put this in gitignore.  I also created my procfile and my requirements.txt file.
12. I then built my allrecipeslist page so that my recipes would display on the screen.  Initially I used accordian format from 
    materializecss but then changed the display to cards on the advice of my mentor.  I checked that the allrecipeslist page worked,
    and that summary information was displayed on the front of the card with a picture of the recipe, and on clicking on the three dot icon
    on the right hand top side of the card, the flip side of the card would then be shown together with the ingredients and method for
    making the recipe.
13. I then put together my addrecipes and editrecipes pages using addrecipes page as a template for my editrecipes page.
14. I checked that both my addrecipes and editrecipes pages worked ensuring that a user could add a recipe and only the author of the recipe
    could edit a recipe.
15. I returned to my allrecipeslist page and put in a link to my islands collections so that users could find out more about
    the island a recipe came from.  This involved building an island page which displayed a picture of the island, a picture of the map of
    the caribbean and some information about the island.  Users checked that this worked.
16. Finally I built my findrecipe page.  This enabled a user to find a recipe which was either a lunch, dinner or dessert recipe, or to find a recipe which 
    contained meat, fish, vegetables or sugar.  Users could also search for recipes which came from speificifed islands, or search for 
    recipes which did not contain specified allergens.  As part of this I created a results page which displayed the results of each
    search.
17. I then  created a login and register page.  The login page allowed registered users to access the app, and if a user was not registered, then
    the register page enabled them to register.
18. Lastly I checked that the entire app worked before doing a final push to heroku, making sure that my environment variables were correctly
    input into the heroku dashboard for the app and that debug was set to false so that the app was secure.
19.  My mentor had a look at my project and advised some changes, so I needed to set debug to true in my cloud9 editor whilst I made these
    changes, then I needed to remember to set debug back to false before pushing to heroku again.
20.  Finally I created a favicon for my app, using a [freefavicom creator](https://www.freefavicon.com/freefavicons/)



## Deployment

The following section describes the process I undertook to deploy this project to Heroku.

* I ensured that all required technologies were installed locally, as per the requirements.txtfile.
* I ensured that I had created a procfile indicating that my app was based on python.
* I used the bash terminal to log in to Heroku, using 'heroku login' command. Input Heroku login details.
* I then created a new Heroku app, using `heroku apps:create appname` command.
* I pushed my  project to Heroku, using `push -u heroku master` command.
* Then I created scale, using `heroku ps:scale web=1` command.
* I then logged into Heroku and selected newly created app.
* I then selected settings. Select 'Reveal Config'.  I then added IP 0.0.0.0 and PORT 5000.
* Then from the 'More' menu on the top right,  I selected 'Restart all dynos'.
* To view my app, in settings I selected the  Domain URL, NOT Git URL to view your hosted application.
* I checked that my app was now deployed via Heroku

## Credits

Content
The text for the islands was copied from wikpaedia.

Media
The photos used in this site were obtained from pixabay and pixels. 
All the photos used in my database were obtained from google images.  These do not require creditation as they 
are used for educational purposes only. 

Acknowledgements
I received inspiration for this project from my mentor Simen Daehlin, fellow students especially Jo Wings,
Miro, John Lynch and John Longatty.  Family, friends and my teaching colleagues and school students were also very helpful 
in giving me feedback.  I used pymongo and flask documentation to help me get my code correct.


