import os

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




@app.route("/")
#@login_required
def index():
    return render_template("index.html")


@app.route("/video")
#@login_required
def video():
    # Put it into database?
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
    return render_template("video.html", video=video_url[1])


@app.route("/notes")
def notes():
    return render_template("notes.html")


@app.route("/slides")
def slides():
    return render_template("slides.html")


@app.route("/source")
def source():
    # List to hold all source files per lecture
    source = []

    # Which lecture
    lecture = "src1"
    path = (f"static/files/source/{lecture}")
    # Open folder, add files to the list
    for f in os.listdir(path):
        with open(os.path.join(path, f)) as f:
            source.append(os.path.basename(f.name))

    return render_template("source.html", source=source)