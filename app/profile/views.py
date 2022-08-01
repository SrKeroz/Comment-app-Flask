from flask import render_template, session

# firebase
from app.firestore_service import get_comment

from . import profile

@profile.route("/<user_id>")
def profile(user_id):
    username = session.get("username")
    context = {
        "get_comment": get_comment(user_id=username),
        "username": username
    }
    if user_id == username:
        return render_template("profile.html", **context)
    
    return render_template("404.html")