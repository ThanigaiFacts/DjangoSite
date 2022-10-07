from django.http import HttpResponse
from django.shortcuts import redirect,render

def index(request):
    return redirect("User/home")

def handler404(request, exception):
    context = {}
    response = render(request, "404.html", context=context)
    response.status_code = 404
    return response