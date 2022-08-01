import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

project_id = 'app-todo-produccion'

cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': project_id,
})


db = firestore.client()

def get_user():
    return db.collection('users').get()

def get_comment(user_id):
    return db.collection("users").document(user_id).collection("frases").get()
