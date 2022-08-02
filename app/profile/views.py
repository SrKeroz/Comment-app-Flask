from flask import render_template, session, redirect, url_for

# login manager
from flask_login import login_required, current_user

# firebase
from app.firestore_service import get_comment
from app.firestore_service import get_user

from . import profile

@profile.route("/profile")
def my_profile():
    user_id = current_user.id

    return redirect(url_for("profile.profile", user_id=user_id))
    

@profile.route("/<user_id>")
def profile(user_id):
    username = get_user(user_id)
    user_id = username.id
    context = {
        "get_comment": get_comment(user_id=user_id),
        "username": user_id
    }

    if username.to_dict() is not None:
        return render_template("profile.html", **context)
    
    return render_template("404.html")