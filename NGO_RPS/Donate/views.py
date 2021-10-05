from . import config
from django.shortcuts import render
from django.http import HttpResponse
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate(config.firebaseConfig)
firebase_admin.initialize_app(cred)
db=firestore.client()



def home(request):
    a=db.collection(u'demo').document(u'a').get().to_dict()
    # db.collection("demo").add({"abc":40})
    print(a)
    return render(request, "home.html",{"a":a})


# Create your views here.
