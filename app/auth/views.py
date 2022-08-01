# flask
from flask import render_template, redirect, url_for, session, flash
from flask_login import login_user, current_user

# Directory
from . import auth
from app.firestore_service import get_user
from app.models import UserData, UserModel

# forms
from app.forms import UserLogin


@auth.route("/login", methods=["GET", "POST"])
def login():
    login_form = UserLogin()
    context = {
        "login_form": login_form
    }
    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data
        

        user_doc = get_user(username)

        # lets check if the user exists
        if user_doc.to_dict() is not None:
            password_from_db = user_doc.to_dict()["password"]
            
            print(password)
            # lets check if the password is correct
            if password_from_db == password:
                user_data = UserData(username, password)
                user_model = UserModel(user_data)
    
                login_user(user_model)


                flash('Well done! Bienvenido', "alert alert-success alert-dismissible")
                return redirect(url_for("index"))
            else:
                flash('Oops! Password incorrecto', 'alert alert-danger alert-dismissible')
        else:
            flash('Warning! El usuario no existe', 'alert alert-warning alert-dismissible')

    return render_template("login.html", **context)