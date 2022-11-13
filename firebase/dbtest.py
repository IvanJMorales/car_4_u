# Initialize database
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Application Default credentials are automatically created.

cred = credentials.Certificate("firebaseCred.json")
app = firebase_admin.initialize_app(cred)
db = firestore.client()


doc_ref = db.collection(u'Cars').document(u'Car Data')
doc_ref.set({
    u'first': u'Ada',
    u'last': u'Lovelace',
    u'born': 1815
})