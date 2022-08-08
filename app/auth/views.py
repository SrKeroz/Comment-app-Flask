# flask
from flask import render_template, redirect, url_for, session, flash
from flask_login import login_user, current_user, login_required, logout_user

# Directory
from . import auth
from app.firestore_service import get_user
from app.firestore_service import register_user
from app.models import UserData, UserModel

# forms
from app.forms import UserLogin, SignupForm

# wekzeug
from werkzeug.security import generate_password_hash, check_password_hash


@auth.route("/login", methods=["GET", "POST"])
def login():
    login_form = UserLogin()
    context = {
        "login_form": login_form
    }
    
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if login_form.validate_on_submit():
        username = login_form.username.data.lower()
        password = login_form.password.data
        

        user_doc = get_user(username)

        # lets check if the user exists
        if user_doc.to_dict() is not None:
            password_from_db = user_doc.to_dict()["password"]
            
            # lets check if the password is correct
            if check_password_hash or password(user_doc.to_dict()["password"], password):
                user_data = UserData(username, password)
                user_model = UserModel(user_data)
    
                login_user(user_model)


                flash('Welcome!', "alert alert-success alert-dismissible")
                return redirect(url_for("index"))
            else:
                flash('Oops! Wrong Password', 'alert alert-danger alert-dismissible')
        else:
            flash("Warning! The user doesn't exist", 'alert alert-warning alert-dismissible')

    return render_template("login.html", **context)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Come Back soon!", "alert alert-info alert-dismissible")
    return redirect(url_for("index"))


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    signup_form = SignupForm()
    context = {
        "signup_form": signup_form

    }
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if signup_form.validate_on_submit():
        username = signup_form.username.data.lower()
        password = signup_form.password.data

        user_doc = get_user(username)

        if user_doc.to_dict() is None:

            password_hash = generate_password_hash(password)
            user_data = UserData(username, password_hash)

            register_user(user_data)

            user_model = UserModel(user_data)
    
            login_user(user_model)

            return redirect(url_for('index'))

            flash('You has been registered successfully')
        else:
            flash('Username already register', 'alert alert-danger alert-dismissible')
        



    return render_template("signup.html", **context)