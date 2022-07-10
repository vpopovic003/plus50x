from http.client import responses
from flask import Flask, render_template, redirect
from flask_session import Session
import sqlite3

from helpers import login_required

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

app.config["SESSION_PERANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

conn = sqlite3.connect("plus50.db")
db = conn.cursor()

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headres["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return responses


@app.route("/")
@login_required
def index():

    return render_template("index.html")
    