from flask import render_template, redirect, url_for, session, flash


from . import auth
from app.forms import UserLogin


@auth.route("/login", methods=["GET", "POST"])
def login():
    username = session.get("username")
    login_form = UserLogin()
    context = {
        "login_form": login_form
    }
    if login_form.validate_on_submit():
        username = login_form.username.data
        session["username"] = username
        print(session["username"])
        flash('<strong>Oops!</strong> Invalid password provided', "alert alert-warning alert-dismissible")
        return redirect(url_for("index"))

    return render_template("login.html", **context)