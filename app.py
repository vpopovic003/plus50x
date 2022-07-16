import os

from http.client import responses
from flask import Flask, render_template, redirect


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("video.html")

"""
@app.route(f"/lecture{lecture_index}")
def lecture():
    return redirect("video.html", lecture_index=lecture_index)
"""


@app.route("/video")
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
    notes = "files/notes/lecture1.html"
    return render_template("notes.html", notes=notes)


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


@app.route("/transcript")
def transcript():
    return render_template("transcript.html")


@app.route("/shorts")
def shorts():
    l1_shorts = [
        "https://www.youtube.com/embed/Fc9htmvVZ9U",
        "https://www.youtube.com/embed/f1xZf4iJDWE",
        "https://www.youtube.com/embed/1wsaV5nVC7g",
        "https://www.youtube.com/embed/WgX8e_O7eG8",
        "https://www.youtube.com/embed/BnJ013X02b8"
    ]
    return render_template("shorts.html", shorts=l1_shorts)

@app.route("/pset0")
def pset0():
    return render_template("pset0.html")

@app.route("/pset1")
def pset1():
    return render_template("pset1.html")