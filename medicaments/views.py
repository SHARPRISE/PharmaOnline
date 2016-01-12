from django.contrib import messages
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from accounts.models import PharmacyUser

from haystack.forms import SearchForm

from .models import Medicament, Famille, Compagnie

# Create your views here.

def MedicamentHome(request):
    form = SearchForm
    template = 'medicament/med_home.html'
    context = {
        "form": form,
        "Submit-btn": "Rechercher",
    }
    return render(request, template, context)

class MedicamentList(ListView):
    model = Medicament
    template_name = "medicaments/med_list.html"

class MedicamentDetail(DetailView):
    model = Medicament
    template_name = "medicaments/detail.html"

    def get_context_data(request, *args, **kwargs):
        context = super(MedicamentDetail,self).get_context_data(*args, **kwargs)
        medicament = self.get_object()
        return context

def MedicamentCreate(request):
    form = MedicamentForm(request.POST or None)
    if form.is_valid():
        medicament = form.save(commit=False)
        medicament.user = request.user
        medicament.save()

        messages.success(request, messages.INFO, "Medicament ajoute.")
    template = "medicaments/med_create.html"
    context = {
        "form": form,
    }
    return render(request, template, context)

def MedicamentUpdate(request):
    medicament = get_object_or_404(Medicament, id=object_id)
    form = MedicamentForm(request.POST or None, instance=medicament)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

        messages.info(request, "Le medicament a ete modifie.")
    template = "medicaments/med_update.html"
    context = {
        "form": form,
        "object": medicament,
    }
    return render(request, template, context)
