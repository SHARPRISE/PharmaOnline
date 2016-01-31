from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from accounts.models import PharmacyUser

from .models import Medicament, Famille, Compagnie
from .forms import MedicamentForm

# Create your views here.

def MedicamentHome(request):
    template = 'accounts/account_base.html'
    context = {
        "form": form,
        "Submit-btn": "Rechercher",
    }
    return render(request, template, context)

#MEDICAMENTS
#Vues de Creation et de modification
def MedicamentCreate(request):
    form = MedicamentForm(request.POST or None)
    if form.is_valid():
        medicament = form.save(commit=False)
        medicament.user = request.user
        medicament.save()

        messages.success(request, "Medicament ajoute.")
    template = "medicaments/med_create.html"
    context = {
        "form": form,
    }
    return render(request, template, context)

def MedicamentUpdate(request, id=None):
    instance = get_object_or_404(Medicament, id=id)
    form = MedicamentForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        instance.info(request, "Le medicament a ete modifie.")
        return HttpResponseRedirect(instance.get_absolute_url())
    template = "medicaments/med_update.html"
    context = {
        "form": form,
        "instance": instance,
    }
    return render(request, template, context)


#vues de liste
class MedicamentList(ListView):
    model = Medicament
    template_name = "medicaments/med_list.html"

    #def get_context_data(self, **kwargs):
    #    context = super(MedicamentList, self).get_context_data(**kwargs)
    #    context['']

def public_med_list(request):
    queryset = Medicament.objects.all()
    template = "medicaments/produits_test.html"
    context = {
        "queryset": queryset,
    }
    return render(request, template, context)

def personal_med_list(request):
    queryset = Medicament.objects.filter(user= request.user)
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter()
    template = "medicaments/produits_test.html"
    context = {
        "queryset": queryset,
    }
    return render(request, template, context)


#vues des elements individuellement
class MedicamentDetail(DetailView):
    model = Medicament
    template_name = "medicaments/detail.html"
