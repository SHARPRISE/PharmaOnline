from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import MessageContact

# Create your views here.
@login_required
def contact(request):
	title = "Contactez-nous maintenant!"
	form  = MessageContact(request.POST or None)
	context= {
            "title": title,
            "form": form
    }
	if form.is_valid():
		instance = form.save(commit = False)
		name = form.cleaned_data.get("Last_name")
		if not name:
			name = "Nouveau nom de Famille"
			instance.name = name
			instance.save()
			context = {
				"title": "Merci"
			}
		if request.user.is_authenticated and request.user.is_staff:
			queryset = ContactModel.objects.all().order_by('-timestamp')
			context = {
				"queryset": queryset
			}

	return render(request, "website/contact.html", context)
