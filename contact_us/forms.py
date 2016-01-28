from django import forms
from .models import PharmaMonkey

class MonkeyForm(forms.ModelForm):
    class Meta:
        model  = PharmaMonkey
        exclude = ['picture']

        def clean_nom(self):
            nom = self.cleaned_data.get('nom')
            if not nom:
                raise forms.ValidationError("Entrez un Monkey")

            else:
                return nom

        def clean_bio(self):
            bio = self.cleaned_data.get('bio')
            if not bio:
                raise forms.ValidationError("Origine du Monkey ou quelques mots sur l'individu")
            else:
                return bio
