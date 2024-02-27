from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from .forms import NewTaskForm
from .forms import EditTaskForm

# Create your views here.

tasks = ["foo", "bar", "fun"]

def taskList(request):
    
    if 'tasks' not in request.session:
        request.session['tasks'] = []

    return render(request, "tasks.html", {
        "tasks" : request.session["tasks"],
        "formEdit" : EditTaskForm()
    })

def addTask(request):

    if request.method == "POST":
        task = request.POST.get("task")

        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]

            return HttpResponseRedirect(reverse("tasks:home"))
    
    return render(request, "add.html", {
        "form" : NewTaskForm()
    })

# def editTask(request):
#     if request.method == "POST":
#         task = request.POST.get("newTask")
#         taskNum = request.POST.get("listNum")
#         taskList = request.session["tasks"]
#         print(task)
#         print(taskNum)

#         oldTask = request.session["tasks"][int(taskNum) - 1]
#         print(oldTask)

#         request.session["tasks"][int(taskNum) - 1] = task

#         form = EditTaskForm(request.POST)
#         if form.is_valid():
#             task = form.cleaned_data("newTask")
#             taskNum = form.cleaned_data("listNum")

#             taskList[taskNum] = task
#             request.session["tasks"] = [taskList]
#             print(request.session["tasks"])

#             return HttpResponseRedirect(reverse("tasks:home"))
            
#     return render(request, "tasks.html", {
#         "form" : EditTaskForm(),
#         "tasks" : request.session["tasks"]
#     })

def clearSesh(request):
    request.session['tasks'] = []
    return render(request, "tasks.html", {
        "tasks" : request.session["tasks"]
    })

def editTask(request):
    if request.method == "POST":    

        taskNum = request.POST.get("taskNum")
        updateTask = request.POST.get("updateTask")

        form = EditTaskForm(request.POST)
        if form.is_valid():
            updateTask = form.cleaned_data["updateTask"]
            taskNum = form.cleaned_data["taskNum"]
            request.session["tasks"][int(taskNum) - 1] = updateTask
            print(updateTask)
            print(taskNum)
            print(request.session["tasks"][int(taskNum) - 1])

            return HttpResponseRedirect(reverse("tasks:home"))
        else:
            print("form not valid")

    return render(request, "tasks.html", {
        "formEdit" : EditTaskForm()
    })