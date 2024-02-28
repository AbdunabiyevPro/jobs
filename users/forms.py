from django import forms

from users.models import UsersModel


class RegistrationForms(forms.ModelForm):
    name = forms.CharField(max_length=128)
    email = forms.CharField(max_length=128)

    class Meta:
        model = UsersModel
        fields = '__all__'