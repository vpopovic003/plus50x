import os
from flask import Flask, render_template, redirect


app = Flask(__name__)


@app.route("/")
def index():
    return redirect("lecture0")


@app.route("/lecture<index>")
def lecture(index):
    videos = [
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
    # Put it into database?
    return render_template("video.html", video=videos[int(index)], index=index)


@app.route("/notes<index>")
def notes(index):
    notes = "files/notes/lecture1.html"
    return render_template("notes.html", notes=notes, index=index)


@app.route("/slides<index>")
def slides(index):
    return render_template("slides.html", index=index)


@app.route("/source<index>")
def source(index):
    # List to hold all source files per lecture
    source = []

    # Which lecture
    lecture = "src1"
    path = (f"static/files/source/{lecture}")
    # Open folder, add files to the list
    for f in os.listdir(path):
        with open(os.path.join(path, f)) as f:
            source.append(os.path.basename(f.name))
    return render_template("source.html", source=source, index=index)


@app.route("/transcript<index>")
def transcript(index):
    return render_template("transcript.html")


@app.route("/shorts<index>")
def shorts(index):
    l1_shorts = [
        "https://www.youtube.com/embed/Fc9htmvVZ9U",
        "https://www.youtube.com/embed/f1xZf4iJDWE",
        "https://www.youtube.com/embed/1wsaV5nVC7g",
        "https://www.youtube.com/embed/WgX8e_O7eG8",
        "https://www.youtube.com/embed/BnJ013X02b8"
    ]
    return render_template("shorts.html", shorts=l1_shorts, index=index)


@app.route("/problems<index>")
def pset0(index):
    return render_template("problems.html", index=index)


@app.route("/pset1<index>")
def pset1(index):
    return render_template("pset1.html", index=index)