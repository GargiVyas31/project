from django.shortcuts import render
import pyrebase
from firebase_admin import credentials
config={
    'apiKey': "AIzaSyAjR7Zu_ruf7twHyMh-OXr183t-TceVvTY",
    'authDomain': "webst-c384e.firebaseapp.com",
    'databaseURL': "https://webst-c384e.firebaseio.com",
    'projectId': "webst-c384e",
    'storageBucket': "webst-c384e.appspot.com",
    'messagingSenderId': "251406846010",
    #'serviceAccount': "C:/Users/maitr/Downloads/webst-c384e-firebase-adminsdk-d2hqm-fcb62dae59.json",

    }

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

database=firebase.database()
# Create your views here.
def mainprofile(request):
	
	
	#print(database.child("teacher").child(Environment.uid).get().val())
	return  render(request,'Teachers/mainpage.html')
    


def editprofile(request):
	
	return render(request,'Teachers/editpage.html')

    
