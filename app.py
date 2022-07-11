from http.client import responses
from flask import Flask, render_template, redirect
from flask_session import Session
import sqlite3

#from helpers import login_required

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

app.config["SESSION_PERANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

conn = sqlite3.connect("plus50.db")
db = conn.cursor()

video_url = [
    "https://www.youtube.com/embed/4zy0z5W0-w4",
    "https://www.youtube.com/embed/Na2wiHOnzXU",
    "https://www.youtube.com/embed/xC3BZa1pcsY",
    "https://www.youtube.com/embed/EXnHX-6voug",
    "https://www.youtube.com/embed/l-dHFS_Pnzc",
    "https://www.youtube.com/embed/urRlbmW5Txw",
    "https://www.youtube.com/embed/k9RO-eEF9xo",
    "https://www.youtube.com/embed/1YVIBFODn58",
    "https://www.youtube.com/embed/lp-FwJwCqpE",
    "https://www.youtube.com/embed/mlRlDFAyPtE",
    "https://www.youtube.com/embed/oe-Iz0j1n6I"
]

@app.route("/")
#@login_required
def index():
    return render_template("index.html")

@app.route("/video")
#@login_required
def video():
    return render_template("video.html", video=video_url[1])

@app.route("/notes")
#@login_required
def notes():
    return render_template("notes.html")
    