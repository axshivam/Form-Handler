from django.shortcuts import render
from django.http import HttpResponse
from . forms import RegistrationForm

def index(request):
    form=RegistrationForm()
    context={
        "myregistrationform":form
    }
    return render(request,"base/index.html",context)

def introduction(request):
    return HttpResponse("<h2>I am shiv sharma</h2>")
