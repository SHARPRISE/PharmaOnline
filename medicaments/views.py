#django
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse_lazy


from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import generics, permissions

from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

#other apps
from accounts.models import PharmacyUser

#third-party apps
from haystack.forms import SearchForm
from haystack.generic_views import SearchView

#medicaments
from .models import Medicament, Famille, Compagnie
from .forms import MedicamentForm
from .serializers import MedicamentSerializer
from .permissions import IsOwner

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

# @login_required
# def create_medicament(request):
#     form = MedicamentForm(request.POST or None)
#     if form.is_valid():
#         medicament = form.save(commit=False)
#         medicament.user = request.user
#         medicament.save()
#
#         messages.success(request, "Medicament ajoute.")
#     template = "medicaments/med_create.html"
#     context = {
#         "form": form,
#     }
#     return render(request, template, context)

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

def public_med_list(request):
    queryset = Medicament.objects.all()
    paginator = Paginator(queryset, 10)
    template = "medicaments/public_list.html"

    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        "queryset": queryset,
    }
    return render(request, template, context)


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
class MedicamentDelete(DeleteView):
    model = Medicament
    success_url = reverse_lazy('inventaire')

class MedicamentCreate(CreateView):
    model = Medicament
    # fields = ('commercial', 'generique', 'quantite', 'description', 'famille', 'stock', 'image')
    success_url = reverse_lazy('ajouter')
    form_class = MedicamentForm
    template_name = 'medicaments/med_create.html'

class CreateView(generics.ListCreateAPIView):
    queryset = Medicament.objects.all()
    serializer_class = MedicamentSerializer
    permission_class = (permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save(user=self.request.user)


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Medicament.objects.all()
    serializer_class = MedicamentSerializer
    permission_class = (permissions.IsAuthenticated, IsOwner)
