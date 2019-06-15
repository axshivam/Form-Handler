from django.shortcuts import render
from django.http import HttpResponse
from . forms import RegistrationForm
from . models import MyformData

def index1(request):
    all_form =  MyformData.objects.all()
    context = {
    "shiv":all_form
    }
    return render(request, "base/db.html", context)

def index(request):
    form=RegistrationForm()
    context={
        "myregistrationform":form
    }
    return render(request,"base/index.html",context)

def introduction(request):
    email=request.POST.get('email')
    first=request.POST.get('first_name')
    last=request.POST.get('last_name')
    c = MyformData(first2=first, last2=last, email2=email)
    c.save()
    all_form =  MyformData.objects.all()
    context = {
    "shiv":all_form
    }
    return render(request, "base/db.html", context)
    #context={
    #"my_email": email,
    #"myfirstname": first,
    #"mylastname":last
    #}
    #return render(request,"base/home.html",context)
