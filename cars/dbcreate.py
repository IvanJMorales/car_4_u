#Imports for database
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import config as cfg

config = cfg.config

def dbcreate():
    cred = credentials.Certificate(config)
    app = firebase_admin.initialize_app(cred)
    db = firestore.client()
    return db


def dbinsert(database,carid,data):
    database.collection(u"Vehicles").document(f"Car #{carid}").set(data)

