from django import forms
from .models import Medicament, Famille, Compagnie

class MedicamentForm(forms.ModelForm):
    commercial= forms.CharField(label="Nom commercial du produit")
    generique = forms.CharField(label="Nom generique du produit")
    quantite  = forms.CharField(label="Contenu de l'unite")
    description = forms.CharField(label="Decrivez le produit", widget=forms.Textarea)
    stock     = forms.CharField(label="Grandeur de votre stock en ce produit")

    class Meta:
        model = Medicament
        fields = [
        'commercial',
        'generique',
        'quantite',
        'description',
        'famille',
        'stock',
        'image',
         ]
    def clean_commercial(self):
        commercial = self.cleaned_data.get('commercial')
        if len(commercial) <= 3:
            raise forms.ValidationError('Le nom du produit est trop court.')
        else:
            return commercial

    def clean_generique(self):
        generique = self.cleaned_data.get('generique')
        if len(generique) <= 3:
            raise forms.ValidationError('Le nom du produit est trop court.')
        else:
            return generique

    def clean_quantite(self):
        quantite = self.cleaned_data.get('quantite')
        if not quantite:
            raise forms.ValidationError("Entrez la quantite (masse/volume/comprimes) de medicament Disponible dans chaque unite")
        else:
            return quantite

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if  not stock:
            raise forms.ValidationError("Veuillez entrer la quantite de medicaments disponibles")
        else:
            return stock

class FamilleForm(forms.ModelForm):
    class Meta:
        model = Famille
        fields = ['nom', 'description']

    def clean_nom(self):
        nom = self.cleaned_data.get('nom')
        if not nom:
            raise forms.ValidationError("Veuillez entrer le nom de la famille de pharmaceutiques")
        else:
            return nom

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if not description:
            raise forms.ValidationError("Veuillez entrer une description de la famille")
        if len(description) < 10:
            raise forms.ValidationError("Description trop courte")
        else:
            return description

class CompagnieForm(forms.ModelForm):
    class Meta:
        model = Compagnie
        fields = ['nom', 'pays']

    def clean_nom(self):
        nom = self.cleaned_data.get('nom')
        if not nom:
            raise forms.ValidationError("Veuillez entrer le nom de la famille de pharmaceutiques")
        else:
            return nom

    def clean_pays(self):
        pays = self.cleaned_data.get('pays')
        if not pays:
            raise forms.ValidationError("Veuillez entrer un pays")
        else:
            return pays
