import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from app.uuid import generate_uuid
from datetime import datetime

project_id = 'app-todo-produccion'

cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': project_id,
})


db = firestore.client()

def get_users():
    return db.collection('users').get()

def get_user(user_id):
    return db.collection("users").document(user_id).get()

def register_user(user_data):
    ref = db.collection("users").document(user_data.username)
    ref.set({"password": user_data.password})



# comment ----------------------------------------------------------------
def get_post():
    ref = db.collection("post").order_by(
    'timezone', direction=firestore.Query.DESCENDING)
    return ref.get()


def get_comment(user_id):
    ref = db.collection("users").document(user_id).collection("frases").order_by(
    'timezone', direction=firestore.Query.DESCENDING)
    return ref.get()


def add_comment(user_id, comment):
    id_frases = generate_uuid()
    comment_collection_ref = db.collection("users").document(user_id).collection("frases").document(id_frases)
    comment_collection_ref.set({"comment": comment, "timezone": datetime.now()})

    post_collection_ref = db.collection("post").document(id_frases)
    post_collection_ref.set({"comment": comment, "user_id": user_id, "timezone": datetime.now()})


def delete_comments(user_id, comment_id):
    comment_collection_ref = db.collection("users").document(user_id).collection("frases").document(comment_id)
    comment_collection_ref.delete()

    comment_collection_ref = db.collection("post").document(comment_id)
    comment_collection_ref.delete()


def update_comments(user_id, comment_id):
    comment_collection_ref = db.collection("users").document(user_id).collection("frases").document(comment_id)
    return comment_collection_ref.get()
    

