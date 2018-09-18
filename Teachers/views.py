from django.shortcuts import render
import pyrebase
from firebase_admin import credentials
config={
     }
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

database=firebase.database()
# Create your views here.
def mainprofile(request):
	
	
	print(database.child("teacher").child(Environment.uid).get().val())
	return  render(request,'Teachers/mainpage.html')
    


def editprofile(request):
	
	return render(request,'Teachers/editpage.html')

    
