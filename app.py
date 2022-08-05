from operator import truediv
import os
from flask import Flask, render_template, redirect, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from cs50 import SQL
import json

import helpers
from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///plus50x.db")


# REGISTER, LOGIN, LOGOUT

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # If clicked submit
    if request.method == "POST":
        # Get all fields
        name = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirmation")

        # Check if all fields filled
        if not name:
            return apology("must provide username")

        if not password:
            return apology("must provide password")

        if not confirm_password:
            return apology("must confirm password")

        # Check if user already exist in the database
        # Query database for 'inputed' username
        rows = db.execute("SELECT * FROM users WHERE username = ?", name)
        # db returns dictionary with 1 row (row 0)
        # Check if rows has exactly one row (found 1 user in database)
        if len(rows) == 1:
            return apology("user already exists")

        # Check if password and confirm passform mathches
        if password == confirm_password:
            # Insert User and password hash into database
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", name, generate_password_hash(password))
            # Add user id to session (log in automatically)
            user_id_rows = db.execute("SELECT id FROM users WHERE username = ?", name)
            session["user_id"] = user_id_rows[0]['id']
            # Add entry into progress table
            db.execute("INSERT INTO progress (user_id) VALUES (?)", session["user_id"])
        else:
            return apology("passwords do not match")

        # Redirect to main page after register
        return redirect("/")

    # If arrived at the page (GET request)
    else:
        return render_template("register.html", index=-1)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return render_template("main.html", index=-2)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html", index=-1)


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

# END REGISTER, LOGIN, LOGOUT


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


@app.route("/lecture<index>", methods=['GET', 'POST'])
def lecture(index):
    if request.method == "POST":
        # Get the currently played video
        information = request.data
        y = json.loads(information)
        video = "video" + y["Video"]
        # Add entry into database
        db.execute("UPDATE progress SET ? = 1 WHERE user_id = ?", video, session["user_id"])
        return ""
    else:
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


@app.route("/shorts<index>", methods=['GET', 'POST'])
def shorts(index):
    if request.method == "POST":
        # Get the currently played video
        information = request.data
        y = json.loads(information)
        short = "shorts" + y["Shorts"]
        # Add entry into database
        db.execute("UPDATE progress SET ? = 1 WHERE user_id = ?", short, session["user_id"])
        return ""
    else:
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
    # Get the index of a key inside dict (change it to list first)
    short_index = list(helpers.shorts[int(index)])
    # Get list index
    short_index = short_index.index(short)
    return render_template("shorts.html", shorts=shorts, index=index, short=short, lecture=helpers.lectures[index], short_index=short_index+1)


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


@app.route("/progress", methods=['GET', 'POST'])
@login_required
def progress():
    if request.method == "POST":
        information = request.data
        y = json.loads(information)
        if "videos" in y:
                videos = y["videos"]
                cvideo = 0
                for videoname in videos:
                    if(videoname == "False"): videoname = 0
                    else: videoname = 1
                    db.execute("UPDATE progress SET video{} = {} WHERE user_id = ?".format(cvideo, videoname), session["user_id"])
                    cvideo += 1
        if "problem" in y:
            problem = y["problem"]
            cproblem = 0
            for videoname in problem:
                if(videoname == "False"): videoname = 0
                else: videoname = 1
                db.execute("UPDATE progress SET pset{} = {} WHERE user_id = ?".format(cproblem, videoname), session["user_id"])
                cproblem += 1
                    
        return ""
    else:
        watchedvideo = []
        watchedshort = ['0']
        for i in range(0,10):
            data = db.execute("SELECT video{} FROM progress WHERE user_id = ?".format(i), session["user_id"])
            watchedvideo.append(data[0]['video{}'.format(i)])
            short_index = list(helpers.shorts[int(i)])

            if (short_index[0] != "no shorts"):
                for c in range(0, len(short_index)):
                    shortdata = db.execute("SELECT shorts{}_{} FROM progress WHERE user_id = ?;".format(i, c + 1), session["user_id"])
                    watchedshort.append(shortdata[0]['shorts{}_{}'.format(i, c + 1)])
        return render_template("progress.html", index=-1, len = 11,lecture=helpers.lectures, shorts = helpers.shorts, watchedvideo = watchedvideo, watchedshort = watchedshort)
