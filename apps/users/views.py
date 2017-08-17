# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User

# the index function is called when root is visited
def index(request):
    # for key, value in request.POST.iteritems():
    #     data =  {
    #         "user":User.objects.all()
    #     }
    return render(request,'users/index.html', {'data':User.objects.all()} )

def create(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/new')
    User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'])
    return redirect('/')


def show(request, id):
    return render(request,'users/show.html', {"data1":User.objects.get(id=id)})

def new(request):
    return render(request,'users/new.html')

def update(request, id):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/edit/'+id)
    else:
        user = User.objects.get(id = id)
        user.first_name = request.POST['first_name']
        user.save()
        user.last_name = request.POST['last_name']
        user.save()
        user.email = request.POST['email']
        user.save()
        return redirect('/')

def edit(request, id):
    return render(request,'users/editusers.html', {"data3":User.objects.get(id=id)})

def delete(request, id):
    b = User.objects.get(id = id)
    b.delete()
    return redirect( '/')