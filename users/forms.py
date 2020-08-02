from django import forms

"""Se crea formulario django para actualizar campos"""


class ProfileForm(forms.Form):
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField()
