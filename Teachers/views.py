from django.shortcuts import render
import pyrebase




# Create your views here.
def mainprofile(request):
	
	
	#print(database.child("teacher").child(Environment.uid).get().val())
	return  render(request,'Teachers/mainpage.html')
    


def editprofile(request):
	
	return render(request,'Teachers/editpage.html')

    
