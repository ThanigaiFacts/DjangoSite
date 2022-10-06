from django.http import HttpResponse
from django.shortcuts import redirect,render

# Create your views here.
def index(request):
    return redirect('home')

def home(request):
    return render(request, "sam.html")