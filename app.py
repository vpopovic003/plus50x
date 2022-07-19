import os
from flask import Flask, render_template, redirect
import helpers


app = Flask(__name__)


@app.route("/")
def index():
    return redirect("lecture0")


@app.route("/lecture<index>")
def lecture(index):
    # Put it into database?
    return render_template("video.html", video=helpers.videos[int(index)], index=index)


@app.route("/notes<index>")
def notes(index):
    notes = f"files/notes/lecture{index}.html"
    return render_template("notes.html", notes=notes, index=index)


@app.route("/slides<index>")
def slides(index):
    return render_template("slides.html", index=index)


@app.route("/source<index>")
def source(index):
    # List to hold all source files per lecture
    source = []
    # Which lecture    
    path = (f"static/files/source/src{index}")
    # Open folder, add files to the list
    for f in os.listdir(path):
        with open(os.path.join(path, f)) as f:
            source.append(os.path.basename(f.name))
    return render_template("source.html", source=source, index=index)


@app.route("/transcript<index>")
def transcript(index):
    return render_template("transcript.html", index=index)


@app.route("/shorts<index>")
def shorts(index):
    # Get the lesson corresponding "Shorts" dictionary
    shorts = helpers.shorts[int(index)]
    # Getting the first value of the corresponding dict
    first = list(helpers.shorts[int(index)].keys())[0]
    return render_template("shorts.html", shorts=shorts, index=index, short=first)


@app.route("/shorts<index>-<short>")
def short(index, short):
    # Get the lesson corresponding "Shorts" dictionary
    shorts = helpers.shorts[int(index)]
    return render_template("shorts.html", shorts=shorts, index=index, short=short)


@app.route("/problems<index>")
def problems(index):
    index = int(index)
    problems = True
    if index == 0:
        path = f"files/problems/pset0.html"
    elif index == 1:
        path = "files/problems/pset1.html"
    elif index > 0 and index < 10:
        path = f"files/problems/lab{index}.html"
        problems = False
    else:
        path = f"files/problems/seminars.html"
    return render_template("problems.html", index=index, problem=path, problems=problems)


@app.route("/problem<index>")
def problem(index):
    path = f"files/problems/pset{index}.html"
    return render_template("problems.html", index=int(index), problem=path, problems=True)