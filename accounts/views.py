from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.core.mail import send_mail, BadHeaderError

from .forms import RegistrationForm, LoginForm

from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def register(request):
    """ Simple registration view for new Pharmacies. """
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        new_user = PharmacyUser()
        new_user.name = name
        new_user.email = email
        new_user.password = set_password(password)
        new_user.save()

    next_url = "/"
    context = {
        "form": form,
        "next_url": next_url,
    }
    return render(request, 'accounts/register.html', context)

def login(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(email=email, password=password)
        if user:
            login(request, user)

            messages.INFO(request, "Bienvenue, %s" %(request.user))
            if next_url:
                return HttpResponseRedirect(next_url)
            else:
                return HttpResponseRedirect('/')
        else:
            raise form.ValidationError("Password and Email do not match. Try again.")
        n_url = reverse("login")
        submit_button = "Login"
        context = {
            "n_url": n_url,
            "submit_button": submit_button,
        }
        return render(request, "accounts/login.html", context)

def logout(request):
    logout(request)
    return HttpResponseRedirect("accounts/logout.html")



def send_email(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['admin@example.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thanks/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')
