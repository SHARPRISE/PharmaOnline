from django.shortcuts import render

# Create your views here.
def landing(request):
    return render("landing.html")

def thanks(request):
    return render("thanks_to.html")
