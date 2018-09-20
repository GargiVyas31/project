from django.shortcuts import render
from .models import Tech_Model,Chem_Model,Elec_Model,Mech_Model,Bio_Model
# Create your views here.
c=0
def tech(request):
    global c
    books = Tech_Model.objects.all()

    if request.method=='POST':
        if 'search_lib' in  request.POST:

            search= request.POST.get('search_lib')
            print("searched ",search)
            s=Tech_Model.objects.filter(book_name__icontains=search.casefold())
            return render(request,'Library/library-tech.html',{'books':s})


        elif "dynid" in request.POST:

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

        else :
            print("book not found")
            return render(request,'Library/library-tech.html',{'books':books})





    print("GET request")

    return render(request,'Library/library-tech.html',{'books':books})


def bio(request):

    books = Bio_Model.objects.all()
    c=0
    if request.method=='POST':
         print("POST request")
         if 'search_lib' in  request.POST:

            search= request.POST.get('search_lib')
            print("searched ",search)
            s=Bio_Model.objects.filter(book_name__icontains=search.casefold())
            return render(request,'Library/library-bio.html',{'books':s})


         elif "dynid" in request.POST:

            print("value of c",c)
            print("Book id",request.POST.get("dynid"))

            t=Bio_Model.objects.filter(id=request.POST.get("dynid") ).values('copies')
            copies= t[0]['copies'] #3
            print("copies initially",copies)

            if  c<3 :
               if (copies>0):
                   copies=copies-1
                   print("Copies later",copies)
                   t=Bio_Model.objects.get( id=request.POST.get("dynid"))
                   t.copies=copies
                   t.save()

               c=c+1

            return render(request, 'Library/library-bio.html',{'books':books})

         else :
            print("book not found")
            return render(request,'Library/library-bio.html',{'books':books})




        #print("GET request")

    return render(request,'Library/library-bio.html',{'books':books})

def elec(request):

    books = Elec_Model.objects.all()
    c=0
    if request.method=='POST':
         print("POST request")
         if 'search_lib' in  request.POST:

            search= request.POST.get('search_lib')
            print("searched ",search)
            s=Elec_Model.objects.filter(book_name__icontains=search.casefold())
            return render(request,'Library/library-elec.html',{'books':s})


         elif "dynid" in request.POST:

            print("value of c",c)
            print("Book id",request.POST.get("dynid"))

            t=Elec_Model.objects.filter(id=request.POST.get("dynid") ).values('copies')
            copies= t[0]['copies'] #3
            print("copies initially",copies)

            if  c<3 :
               if (copies>0):
                   copies=copies-1
                   print("Copies later",copies)
                   t=Elec_Model.objects.get( id=request.POST.get("dynid"))
                   t.copies=copies
                   t.save()

               c=c+1

            return render(request, 'Library/library-elec.html',{'books':books})

         else :
            print("book not found")
            return render(request,'Library/library-elec.html',{'books':books})


    return render(request,'Library/library-elec.html',{'books':books})

def mech(request):

    books = Mech_Model.objects.all()
    c=0
    if request.method=='POST':
         print("POST request")
         if 'search_lib' in  request.POST:

            search= request.POST.get('search_lib')
            print("searched ",search)
            s=Mech_Model.objects.filter(book_name__icontains=search.casefold())
            return render(request,'Library/library-bio.html',{'books':s})


         elif "dynid" in request.POST:

            print("value of c",c)
            print("Book id",request.POST.get("dynid"))

            t=Mech_Model.objects.filter(id=request.POST.get("dynid") ).values('copies')
            copies= t[0]['copies'] #3
            print("copies initially",copies)

            if  c<3 :
               if (copies>0):
                   copies=copies-1
                   print("Copies later",copies)
                   t=Mech_Model.objects.get( id=request.POST.get("dynid"))
                   t.copies=copies
                   t.save()

               c=c+1

            return render(request, 'Library/library-mech.html',{'books':books})

         else :
            print("book not found")
            return render(request,'Library/library-mech.html',{'books':books})


    return render(request,'Library/library-mech.html',{'books':books})

def chem(request):

    books = Chem_Model.objects.all()
    c=0
    if request.method=='POST':
         print("POST request")
         if 'search_lib' in  request.POST:

            search= request.POST.get('search_lib')
            print("searched ",search)
            s=Chem_Model.objects.filter(book_name__icontains=search.casefold())
            return render(request,'Library/library-chem.html',{'books':s})


         elif "dynid" in request.POST:

            print("value of c",c)
            print("Book id",request.POST.get("dynid"))

            t=Chem_Model.objects.filter(id=request.POST.get("dynid") ).values('copies')
            copies= t[0]['copies'] #3
            print("copies initially",copies)

            if  c<3 :
               if (copies>0):
                   copies=copies-1
                   print("Copies later",copies)
                   t=Chem_Model.objects.get( id=request.POST.get("dynid"))
                   t.copies=copies
                   t.save()

               c=c+1

            return render(request, 'Library/library-chem.html',{'books':books})

         else :
            print("book not found")
            return render(request,'Library/library-chem.html',{'books':books})


    return render(request,'Library/library-chem.html',{'books':books})
