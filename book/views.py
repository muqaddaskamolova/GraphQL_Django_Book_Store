from django.http import HttpResponse
from django.shortcuts import render


def catalog(request):
    site_name = "Modern Musician Book"
    response_html = u"<html><body>Welcome to %s.</body></html>" % site_name
    return HttpResponse(response_html)


def home(request):
    return render(request, "index.html", {})
