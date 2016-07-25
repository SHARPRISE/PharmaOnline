from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import MessageContact
from .models import Contact

# Create your views here.
@login_required
def contact(request):
	title = "Contactez-nous maintenant!"
	form  = MessageContact(request.POST or None)
	if form.is_valid():
		instance = form.save(commit = False)
		name = form.cleaned_data.get("Last_name")
		if not name:
			name = "Nouveau nom de Famille"
			instance.name = name
			instance.save()
			messages.success(request, "Formulaire recu")
			return redirect("/")
		else:
			instance.save()
			messages.success(request, "Formulaire recu")
			return redirect("/")
	context= {
        "title": title,
        "form": form,
    }


	return render(request, "contact_us/message_us.html", context)
