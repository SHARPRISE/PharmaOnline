from django.shortcuts import render

# Create your views here.
def landing(request):
    return render(request, "general/cover.html")

def about(request):
    return render(request, "general/about.html")

def dashboard(request):
    return render(request, "general/dashboard.html")
