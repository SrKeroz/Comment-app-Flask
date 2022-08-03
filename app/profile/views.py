from flask import render_template, session, redirect, url_for, flash

# Forms
from app.forms import PublicPost

# login manager
from flask_login import login_required, current_user

# firebase
from app.firestore_service import get_comment
from app.firestore_service import get_user
from app.firestore_service import add_comment

from . import profile

@profile.route("/profile")
def my_profile():
    user_id = current_user.id

    return redirect(url_for("profile.profile", user_id=user_id))
    

@profile.route("/profile/comment", methods=["POST"])
def public_comment():
    public_post = PublicPost()
    context = {
        "public_post": public_post
    }


    if public_post.validate_on_submit():

        add_comment()
        return redirect(url_for('index.html'))




@profile.route("/<user_id>", methods=["POST", "GET"])
def profile(user_id):
    username = get_user(user_id)
    user_id = username.id
    public_post = PublicPost()
    context = {
        "get_comment": get_comment(user_id=user_id),
        "username": user_id,
        "public_post": public_post
    }
    comment = public_post.comment.data

    if public_post.validate_on_submit():
        add_comment(user_id, comment)


        flash("your post has been created successfully", "alert alert-success alert-dismissible")
        return redirect(url_for('profile.my_profile'))

    if username.to_dict() is not None:

        return render_template("profile.html", **context)
    
    return render_template("404.html")