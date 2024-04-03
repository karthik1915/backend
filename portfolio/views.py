import json
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from .utils import ContactMessage


def index(req):
    return render(req, "main.html")


def about(req):
    return render(req, 'about.html')


@csrf_exempt
def contact(request):
    if request.method == "POST":
        data = json.loads(request.body)
        if (ContactMessage(data)):
            print("success")
        else:
            print("failed")
    return render(request, 'contact.html')


def services(req):
    return render(req, 'services.html')
