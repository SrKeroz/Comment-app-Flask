from flask import render_template, session, redirect, url_for, flash, json, request

# Forms
from app.forms import PublicPost, UpdatePost

# login manager
from flask_login import login_required, current_user

# firebase
from app.firestore_service import get_comment
from app.firestore_service import get_user
from app.firestore_service import add_comment
from app.firestore_service import delete_comments
from app.firestore_service import update_comments

from . import profile

@profile.route("/profile")
def my_profile():
    user_id = current_user.id

    return redirect(url_for("profile.profile", user_id=user_id))
    

@profile.route("/profile/comment/delete/<comment_id>", methods=["GET","POST"])
def delete_comment(comment_id):
    user_id = current_user.id
    delete_comments(user_id, comment_id)

    flash("Your post has been successfully deleted.", "alert alert-success alert-dismissible")

    return redirect(url_for("profile.profile", user_id=user_id))


@profile.route("/profile/comment/update/", methods=["POST"])
def update_comment():
    user_id = current_user.id
    comment = request.json["comment"]
    id = request.json["id"]
    update_comments(user_id, id, comment)
    flash("Your comment has been updated successfully")
    return redirect(url_for("profile.profile", user_id=user_id))



@profile.route("/<user_id>", methods=["POST", "GET"])
def profile(user_id):
    username = get_user(user_id)
    user_id = username.id
    public_post = PublicPost()
    update_post = UpdatePost

    context = {
        "get_comment": get_comment(user_id=user_id),
        "username": user_id,
        "public_post": public_post,
        "update_post": update_post
    }
    comment = public_post.comment.data

    if public_post.validate_on_submit():
        add_comment(user_id, comment)


        flash("Your post has been created successfully", "alert alert-success alert-dismissible")
        return redirect(url_for('profile.my_profile'))

    if username.to_dict() is not None:

        return render_template("profile.html", **context)
    
    return render_template("404.html")