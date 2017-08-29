# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login_app.models import User, Task
from django.shortcuts import render, redirect
# from models import User
from django.contrib import messages
from datetime import datetime
from django.db.models import Q
# Create your views here.

# def test(request):
#     print "***appointment_app views urls***"

def seshCheck(request):
    try:
        return request.session['user_id']
    except:
        return False

def index(request):
    if seshCheck(request) == False:
        return redirect("/")
    # today = datetime.today()  

    context = {
        "tasks": Task.objects.all().filter(planned_by= request.session['user_id']).filter(date__range=["2017-08-29", "2017-08-30"]).order_by('time'),
        "far": Task.objects.all().filter(planned_by= request.session['user_id']).exclude(date__range=["2017-08-29", "2017-08-30"]).order_by('date'),
        "time": datetime.now(),
    }

    return render(request, "appointment_app/dash.html", context)

def updatep(request, id):
    if seshCheck(request) == False:
        return redirect("/")

    context = {
        "tasks": Task.objects.all().get(id=id)
    }
    return render(request, "appointment_app/update.html", context)

def addtask(request):
    
    results = Task.objects.tVal(request.POST)

    if len(results["errors"]) > 0:
        for error in results["errors"]:
            messages.error(request, error)

        return redirect('/appointment')
    messages.success(request, "success, your appointment has been added")

    user = User.objects.get(id= request.session["user_id"])
    task = Task.objects.create(date=request.POST['date'], time = request.POST["time"], planned_by=User.objects.get(id=request.session['user_id']), tasks=request.POST['tasks'])
    # trip.user.add(User.objects.get(id=request.session["user_id"]))
    # destination = Trip.objects.tcreator(request.POST)
    return redirect('/appointment') 

def update(request, id):
    # task = Task.objects.get(id=id)
    # print id
    results = Task.objects.tVal(request.POST)

    if len(results["errors"]) > 0:
        for error in results["errors"]:
            messages.error(request, error)
        return redirect('/appointment')
    Task.objects.filter(id= id).update(tasks= request.POST['tasks'], date= request.POST['date'], time= request.POST['time'], status= request.POST['status'])
    return redirect('/appointment')

def remove(request, id):
    Task.objects.filter(id = id).delete()
    # Task.objects.get(id= id).tasks.remove(id = id)
    return redirect("/appointment")

# def uperror(request):
#     if seshCheck(request) == False:
#         return redirect("/")

#     context = {
#         "tasks": Task.objects.all().get(id=id)
#     }
#     return render(request, "appointment_app/update.html", context)