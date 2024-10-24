from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def func1(request):
    good_students=[
      {'name':"person1","mobile":123123,"role":"Manager"},
      {'name':"person2","mobile":234234,"role":"Accountant"},
      {'name':"person3","mobile":345345,"role":"HR"},
      {'name':"person4","mobile":456456,"role":"Student"}
   ]
    return render(request,"index.html", {'students':good_students})

def func2(request):
    return render(request,"about.html")


def func3(request):
    return render(request,"contact.html")
