import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session, url_for


app = Flask(__name__)
app.secret_key = "randomstring123"


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



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)