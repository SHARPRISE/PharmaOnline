from django import forms
from .models import PharmacyUser, Pharmacy, NormalUser

class AdminRegistration(forms.ModelForm):

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = PharmacyUser
        fields = ['name', 'email', 'password']

    def clean_password(self):
        password1 = self.cleaned_data.get("password1")

        if len(password1) < 7:
            raise forms.ValidationError("Mot de Passe trop court.")

        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Les mots de passe ne concordent pas.")

        return password2

    def clean_name(self):
        name = self.cleaned_data.get('name')
        try:
            exists = PharmacyUser.objects.get(name=name)
            raise forms.ValidationError("This Pharmacy Already Exists.")
        except PharmacyUser.DoesNotExist:
                return(name)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            exists = PharmacyUser.objects.get(email=email)
            raise forms.ValidationError("This email is already in use.")
        except PharmacyUser.DoesNotExist:
            return email

    def save(self, commit=True):
        user = super(AdminRegistration, self).save(commit=False)
        user.set_password(self.cleaned_data.get["password1"])
        if commit:
            user.save()
        return user

class CreateUser(forms.ModelForm):

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = PharmacyUser
        fields = ['name', 'email', 'password']

    def clean_password(self):
        password1 = self.cleaned_data.get("password1")

        if len(password1) < 7:
            raise forms.ValidationError("Mot de Passe trop court.")

        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Les mots de passe ne concordent pas.")

        return password2

    def clean_name(self):
        name = self.cleaned_data.get('name')
        try:
            exists = PharmacyUser.objects.get(name=name)
            raise forms.ValidationError("This Pharmacy Already Exists.")
        except PharmacyUser.DoesNotExist:
                return(name)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            exists = PharmacyUser.objects.get(email=email)
            raise forms.ValidationError("This email is already in use.")
        except PharmacyUser.DoesNotExist:
            return email

    def save(self, commit=True):
        user = super(CreateUser, self).save(commit=False)
        user.set_password(self.cleaned_data.get["password1"])
        if commit:
            user.save()
        return user


class RegistrationForm(forms.Form):
    name  = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput())

    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 6:
            raise forms.ValidationError("Password must contain at least 6 characters.")
        #if (password1.islower() or password1.isdigit()):
        #    raise forms.ValidationError("Password must contain at least: n\
        #    1 uppercase letter and 1 number. Try again.")
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("The passwords you have entered do not match.")
        return password1

    def clean_name(self):
        name = self.cleaned_data.get('name')
        try:
            exists = PharmacyUser.objects.get(name=name)
            raise forms.ValidationError("This Pharmacy Already Exists.")
        except PharmacyUser.DoesNotExist:
                return(name)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            exists = PharmacyUser.objects.get(email=email)
            raise forms.ValidationError("This email is already in use.")
        except PharmacyUser.DoesNotExist:
            return email


class PharmacyRegistrationForm(forms.ModelForm):
    """A form for creating Pharmacies. Has to be used in tandem with the
    standard RegistrationForm."""
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = Pharmacy
        exclude = ['user']

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
            return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(PharmacyRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    email = forms.CharField(label="Email")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())
