from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from accounts.models import PharmacyUser

from haystack.forms import SearchForm

from .models import Medicament, Famille, Compagnie
from .forms import MedicamentForm

# Create your views here.

def MedicamentHome(request):
    form = SearchForm
    template = 'accounts/account_base.html'
    context = {
        "form": form,
        "Submit-btn": "Rechercher",
    }
    return render(request, template, context)

class MedicamentList(ListView):
    model = Medicament
    template_name = "medicaments/med_list.html"

    #def get_context_data(self, **kwargs):
    #    context = super(MedicamentList, self).get_context_data(**kwargs)
    #    context['']

class MedicamentDetail(DetailView):
    model = Medicament
    template_name = "medicaments/detail.html"


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
