from django.shortcuts import render


def index(req):
    return render(req, "main.html")


def about(req):
    return render(req, 'about.html')


def contact(req):
    return render(req, 'contact.html')


def services(req):
    return render(req, 'services.html')
