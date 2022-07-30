import os
from flask import Flask, render_template, redirect
import helpers


app = Flask(__name__)


@app.route("/")
def index():
    return redirect("main")


@app.route("/main")
def main():
    return render_template("main.html", index=-1)


@app.route("/video<index>")
def video(index):
    index = int(index)
    shorts = helpers.shorts[index]
    # Put it into database?
    return render_template("video.html", shorts=shorts, video=helpers.videos[int(index)], index=index, lecture=helpers.lectures[index])


@app.route("/lecture<index>")
def lecture(index):
    index = int(index)
    shorts = helpers.shorts[index]
    # Put it into database?
    return render_template("lectures.html",shorts=shorts, video=helpers.videos[int(index)], index=index, lecture=helpers.lectures[index])


@app.route("/notes<index>")
def notes(index):
    index = int(index)
    shorts = helpers.shorts[index]
    notes = f"files/notes/lecture{index}.html"
    return render_template("notes.html" ,shorts=shorts , notes=notes, index=index, lecture=helpers.lectures[index])


@app.route("/slides<index>")
def slides(index):
    index = int(index)
    shorts = helpers.shorts[index]
    return render_template("slides.html", shorts=shorts, index=index, lecture=helpers.lectures[index])

@app.route("/settings")
def settings():
    return render_template("settings.html", index=-1)


@app.route("/source<index>")
def source(index):
    index = int(index)
    shorts = helpers.shorts[index]
    # List to hold all source files per lecture
    source = []
    # Which lecture    
    path = (f"static/files/source/src{index}")
    # Open folder, add files to the list
    if index == 0 or index > 8 or (index > 3 and index < 8):
        source = None
    else:
        for f in os.listdir(path):
            with open(os.path.join(path, f)) as f:
                source.append(os.path.basename(f.name))
    return render_template("source.html", shorts=shorts, source=source, index=index, lecture=helpers.lectures[index])


@app.route("/transcript<index>")
def transcript(index):
    index = int(index)
    shorts = helpers.shorts[index]
    return render_template("transcript.html", shorts=shorts, index=index, lecture=helpers.lectures[index])


@app.route("/shorts<index>")
def shorts(index):
    index = int(index)
    # Get the lesson corresponding "Shorts" dictionary
    shorts = helpers.shorts[index]
    # Getting the first value of the corresponding dict
    first = list(helpers.shorts[index].keys())[0]
    return render_template("shorts.html", shorts=shorts, index=index, short=first, lecture=helpers.lectures[index])


@app.route("/shorts<index>-<short>")
def short(index, short):
    index = int(index)
    # Get the lesson corresponding "Shorts" dictionary
    shorts = helpers.shorts[int(index)]
    return render_template("shorts.html", shorts=shorts, index=index, short=short, lecture=helpers.lectures[index])


@app.route("/problems<index>")
def problems(index):
    index = int(index)
    problems = True
    shorts = helpers.shorts[index]
    if index == 0:
        path = f"files/problems/pset0.html"
    elif index == 1:
        path = "files/problems/pset1.html"
    elif index > 0 and index < 10:
        path = f"files/problems/lab{index}.html"
        problems = False
    else:
        path = f"files/problems/seminars.html"
        problems = False
    return render_template("problems.html", shorts=shorts, index=index, problem=path, problems=problems)


@app.route("/problem<index>")
def problem(index):
    index = int(index)
    problems = True
    shorts = helpers.shorts[index]
    if index < 10:
        path = f"files/problems/pset{index}.html"
    else:
        path = f"files/problems/final.html"
        problems = False 
    return render_template("problems.html",shorts=shorts, index=int(index), problem=path, problems=problems)