from django import forms

from users.models import *


class RegistrationForms(forms.ModelForm):
    name = forms.CharField(max_length=128)
    email = forms.CharField(max_length=128)

    class Meta:
        model = FrontendUsersModel
        fields = '__all__'



class BacRegistrationForms(forms.ModelForm):
    name = forms.CharField(max_length=128)
    email = forms.CharField(max_length=128)

    class Meta:
        model = BackendUsersModel
        fields = '__all__'




class TelegramRegistrationForms(forms.ModelForm):
    name = forms.CharField(max_length=128)
    email = forms.CharField(max_length=128)

    class Meta:
        model = TelegramUsersModel
        fields = '__all__'



class SmmRegistrationForms(forms.ModelForm):
    name = forms.CharField(max_length=128)
    email = forms.CharField(max_length=128)

    class Meta:
        model = GraphicDesignerUsersModel
        fields = '__all__'



class GraphicRegistrationForms(forms.ModelForm):
    name = forms.CharField(max_length=128)
    email = forms.CharField(max_length=128)

    class Meta:
        model = GraphicDesignerUsersModel
        fields = '__all__'




class MobilRegistrationForms(forms.ModelForm):
    name = forms.CharField(max_length=128)
    email = forms.CharField(max_length=128)

    class Meta:
        model = MobilografUsersModel
        fields = '__all__'