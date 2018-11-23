from django import forms

class NameForm(forms.Form):
    Ebom = forms.CharField(label='Your name', max_length=100)