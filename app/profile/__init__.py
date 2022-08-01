from flask import Blueprint

profile = Blueprint("profile", __name__, url_prefix="/p")

from . import views