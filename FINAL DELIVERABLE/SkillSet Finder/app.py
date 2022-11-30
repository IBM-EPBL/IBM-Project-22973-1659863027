from telnetlib import LOGOUT
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/signup")
def signup():
    return render_template('signup.html')

@app.route("/login")
def signin():
    return render_template('login.html')

@app.route("/success")
def success():
    return render_template('success.html')

@app.route("/terms")
def terms():
    return render_template('team&condition.html')