from django.shortcuts import render
from django.http import HttpResponse
from . forms import RegistrationForm
from . models import MyformData
from django.contrib.auth import authenticate, login, logout

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








    #These are function of checking django login Authentication
def user_login(request):
    context ={}
    if request.method == "POST":
        pass
    else:
        return render(request, "auth/login.html", context)


def success(request):
    pass


def user_logout(request):
    pass
