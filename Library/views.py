from django.shortcuts import render
from .models import Tech_Model,Chem_Model,Elec_Model,Mech_Model,Bio_Model
# Create your views here.
c=0
def tech(request):
    global c
    books = Tech_Model.objects.all()

    if request.method=='POST':

        print("value of c",c)
        print("Book id",request.POST.get("dynid"))

        t=Tech_Model.objects.filter(id=request.POST.get("dynid") ).values('copies')
        copies= t[0]['copies'] #3
        print("copies initially",copies)

        if  c<3 :
           if (copies>0):
               copies=copies-1
               print("Copies later",copies)
               t=Tech_Model.objects.get( id=request.POST.get("dynid"))
               t.copies=copies
               t.save()

           c=c+1


        return render(request, 'Library/library-tech.html',{'books':books})


    print("GET request")

    return render(request,'Library/library-tech.html',{'books':books})


def bio(request):

    books = Bio_Model.objects.all()
    if request.method=='POST':
        print("POST request")
        return render(request, 'Library/library-bio.html')


        #print("GET request")

    return render(request,'Library/library-bio.html',{'books':books})

def elec(request):

    books = Elec_Model.objects.all()
    if request.method=='POST':
        print("POST request")
        return render(request, 'Library/library-elec.html')


        #print("GET request")

    return render(request,'Library/library-elec.html',{'books':books})

def mech(request):

    books = Mech_Model.objects.all()
    if request.method=='POST':
        print("POST request")
        return render(request, 'Library/library-mech.html')


        #print("GET request")

    return render(request,'Library/library-mech.html',{'books':books})

def chem(request):

    books = Chem_Model.objects.all()
    #issued = Chem_Model.objects.filter('issued')
    #copies = Chem_Model.objects.filter('copies')



    if request.method=='POST' :
        print("POST request")
        return render(request, 'Library/library-chem.html')


        #print("GET request")

    return render(request,'Library/library-chem.html',{'books':books})
