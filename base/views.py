from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2> Ax Shivam Sharma</h2>")

def introduction(request):
    return HttpResponse("<h2>I am shiv sharma</h2>")
