from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from accounts.models import PharmacyUser

from haystack.forms import SearchForm
from haystack.generic_views import SearchView

from .models import Medicament, Famille, Compagnie
from .forms import MedicamentForm

# Create your views here.

def home(request):
    form = SearchForm
    template = 'medicaments/med_base.html'
    context = {
        "form": form,
        "Submit-btn": "Rechercher",
    }
    return render(request, template, context)

#class ResultView(SearchView):
#    template_name = 'medicaments/results.html'

#MEDICAMENTS
#Vues de Creation et de modification

@login_required
def create_medicament(request):
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

@login_required
def update_medicament(request, pk=None):
    instance = get_object_or_404(Medicament, pk=pk)
    form = MedicamentForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.info(request, "Le medicament a ete modifie.")
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
    template_name = "medicaments/private_list.html"

    #def get_context_data(self, **kwargs):
    #    context = super(MedicamentList, self).get_context_data(**kwargs)
    #    context['']

def public_med_list(request):
    queryset = Medicament.objects.all()
    template = "medicaments/public_list.html"
    context = {
        "queryset": queryset,
    }
    return render(request, template, context)


class PrivateMedList(ListView):
    template_name = "medicaments/private_list.html"

    def get_queryset(self):
        user = self.request.user
        return Medicament.objects.filter(user = user)



@login_required
def personal_med_list(request):
    queryset = Medicament.objects.filter(user= request.user)
    template = "medicaments/private_list.html"
    context = {
        "queryset": queryset,
    }
    return render(request, template, context)


#vues des elements individuellement
class MedicamentDetail(DetailView):
    model = Medicament
    template_name = "medicaments/med_detail.html"


#vues de suppression
#def delete_med(request, id=None):
#    if not request.user.is_staff or request.user.is_superuser:
