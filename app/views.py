from django.shortcuts import render
from app.models import *
# Create your views here.
def index(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def register(request):
    return render(request, "register.html")

def login(request):
    return render(request, "login.html")

def submit(request):
    region = Region.objects.all()
    states = State.objects.all()
    division = Division.objects.all()
    district = District.objects.all()
    return render(request, "submit.html",{"divisions":division,"districts":district})

def view(request):
    return render(request, "view.html")


def submitted(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        resp = request.POST.get('zimmedari')

        Report(zimmedari=resp, zimmedar_name=name).save()

    return render(request, "home.html")