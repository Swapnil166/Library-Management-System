# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import *
from .models import *

def index(request):
        return render(request, "index.html")
def login(request):
    if request.method == "POST":
        e=request.POST.get('emailaddress')
        obj = user.objects.filter(email=e)
        
        
        for i in obj:
             if i is not None:
                global fullname
                fullname=i.fname
                if i.password == request.POST.get('pass'):
                    shelf = bookn.objects.all()
                    context = {'d':shelf,'f':fullname}
                    return render(request, 'admin-page.html', context)
                else:
                     m = "Invalid Password"
                     return render(request, "login.html", {'c': m})
       
        m = "user does not exist"
        return render(request, "login.html", {'c': m})
    else:
        
        return render(request, "login.html")
def reg(request):
    if request.method == "POST":
        users = user(fname=request.POST.get('fname'),
                     password=request.POST.get('pass'),
                     password2=request.POST.get('pass2'),
                     email=request.POST.get('email'))
        users.save()
        return render(request, "signup.html",{'c':'signup successfully'})
    else:
         return render(request, "signup.html")


def adminlog(request):
        if request.method == "POST":
            if request.POST.get('bookinput') != '':
                book = bookn(bookname=request.POST.get('bookinput'))
                book.save()
        shelf = bookn.objects.all()
        j=0
        for i in shelf:
            print(i)
            j=j+1
        a=[]
        for i in range(j+1):
            a.append(i)

        context = {'d':shelf,'f':fullname}

        return render(request, "admin-page.html", context)


def update(request,id):
    if request.method == "POST":
        z = request.POST.get('bookname')
        book = bookn(bookid=id,bookname=z)
        book.save()
        shelf = bookn.objects.all()
        return render(request, 'admin-page.html', {'d': shelf})

    i=bookn.objects.get(pk=id)
    id=i.bookname
    return render(request, "update.html",{'d':id})



def delete(request,id):
    shel = bookn.objects.all()
    for i in shel:
        if i.bookid==id:
            n=i.bookid
            shel = bookn.objects.get(pk=n)
            shel.delete() 
        elif i.bookid>id:
            m=i.bookid-1
            d=i.bookname
            shel = bookn.objects.get(pk=i.bookid)
            shel.delete()
            p=bookn(bookid=m,bookname= d)
            p.save()
            print(i.bookid)
    shelf = bookn.objects.all()
    return render(request, 'admin-page.html', {'d': shelf})

def addbook(request):
    if request.method == "POST":
        z=request.POST.get('bookname')
        s=bookn.objects.all()
        j=1
        k=0
        for i in s:
            if i.bookname==z:
                k=k+1
            j=i.bookid+1
        if k==1:
            return render(request, "addbook.html",{'m':'all ready exist'})
        else:
            book = bookn(bookid=j,bookname = z)
            book.save()
            shelf = bookn.objects.all()
            return render(request, 'admin-page.html',{'d': shelf})
    else:
        return render(request, "addbook.html")
def streg(request):
    if request.method == "POST":
        users = student(fname=request.POST.get('fname'),
                        password=request.POST.get('pass'),
                        password2=request.POST.get('pass2'),
                        email=request.POST.get('email'))
        users.save()
        c='signup sucessfully'
        return render(request,'studentsignup.html',{'c':'signup sucessfully'})
    else:
         return render(request,'studentsignup.html')
def stlog(request):
    if request.method == "POST":
        e=request.POST.get('emailaddress')
        obj = student.objects.filter(email=e)
        for i in obj:
             if i is not None:
                if i.password == request.POST.get('pass'):
                    shelf = bookn.objects.all()
                    return render(request, "stdata.html",{'d': shelf})
                else:
                     m = "Invalid Password"
                     return render(request, "studenlogine.html", {'c': m})
             
        m = "user does not exist"
        return render(request, "studenlogine.html", {'c': m})
    else:
        return render(request, "studenlogine.html")