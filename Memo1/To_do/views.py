from django.shortcuts import render

tasks = ["111", "222", "333"]
# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks,
    })

def add(request):
    return render(request, "task/add.html", )