from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.core.mail import send_mail, BadHeaderError

from .forms import RegistrationForm, LoginForm, CreateUser, PharmacyRegistrationForm
from .models import PharmacyUser, Pharmacy, NormalUser


# Create your views here.
def client_registration(request):
    """ Simple registration view for new clients. """
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password1']
        new_user = PharmacyUser()
        new_user.name = name
        new_user.email = email
        new_user.set_password(password)
        new_user.save()

        messages.success(request, "Bienvenue %s" %(request.user))
        return redirect("/")
    else:
        form = RegistrationForm(request.POST or None)
    next_url = "/"
    context = {
        "form": form,
        "next_url": next_url,
    }
    return render(request, 'accounts/account_register.html', context)

def pharmacy_registration(request):
    """An updated registration form, specifically for pharmacies."""
    pharmacy_form = PharmacyRegistrationForm(request.POST or None)
    register_form = RegistrationForm(request.POST or None)
    if register_form.is_valid() and pharmacy_form.is_valid():
        name = register_form.cleaned_data['name']
        email = register_form.cleaned_data['email']
        password = register_form.cleaned_data['password1']
        new_user = PharmacyUser()
        new_user.name = name
        new_user.email = email
        new_user.set_password(password)
        new_user.save()
        pharmacy = pharmacy_form.save(commit=False)
        pharmacy.user = new_user
        pharmacy.adresse = adresse
        pharmacy.horaire = horaire
        pharmacy.proprietaire = proprietaire
        pharmacy.save()
        return redirect('/')
    context = {
        "register_form": register_form,
        "pharmacy_form": pharmacy_form,
    }
    return render(request, "accounts/pharmacy_register.html", context)

def bridge(request):
    return render(request, 'accounts/account_pre_registration.html')

def auth_login(request):
	form = LoginForm(request.POST or None)
	next_url = request.GET.get('next')
	if form.is_valid():
		email = form.cleaned_data['email']
		password = form.cleaned_data['password']
		user = authenticate(email=email, password=password)
		if user is not None:
			login(request, user)
			if next_url is not None:
				return HttpResponseRedirect(next_url)
			return HttpResponseRedirect("/")

	title = "Login"
	submit_btn = title
	submit_btn_class = "btn-success btn-block"
	context = {
		"form": form,
		"title": title,
		"submit_btn": submit_btn,
		"submit_btn_class": submit_btn_class,
		}
	return render(request, "accounts/account_login.html", context)

def auth_logout(request):
    logout(request)
    messages.info(request, "Vous vous etes deconnectes avec succes.")
    return HttpResponseRedirect(reverse('accounts:login'))



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
