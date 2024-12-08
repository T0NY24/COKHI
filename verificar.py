import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("HubUIDE\hubuide-firebase-adminsdk-4p82r-c015f8b288.json")
firebase_admin.initialize_app(cred)

from firebase_admin import firestore
db = firestore.client()



