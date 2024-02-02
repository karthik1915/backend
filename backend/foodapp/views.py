from django.shortcuts import render


def ping(req):
    return render("<h1>hello</h1>")
