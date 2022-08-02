# flask
from flask import Flask, render_template, url_for, redirect, session, request, flash
from flask_login import current_user

# module
from app import create_app

# forms
from app.forms import UserLogin


#firesbase
from app.firestore_service import get_users
from app.firestore_service import get_comment


app = create_app()

todos = ["manzana", "Pera", "patilla"]

@app.errorhandler(404)
def not_found(error):
    return render_template("404.html", error=error)


@app.route("/")
def index():
    username = None
    if username:
        username = current_user.id
    context={
        "todos": todos,
        "username": username,
        "get_comment": get_comment(user_id=username)

    }

    for user in get_users():
        print(user)


    return render_template("index.html", **context)

if __name__ == "__main__":
    app.run(None, 3000, True)