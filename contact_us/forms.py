from django import forms
from .models import PharmaMonkey, Contact

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


class MessageContact(forms.ModelForm):
    class Meta:
        model  = Contact
        fields = ['first_name', 'Last_name', 'email', 'message', 'msg_subject']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        domain, extension = provider.split('.')
        if not email:
            raise forms.ValidationError("Entrez une adresse email")

        return email
