# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelChoiceField
from .models import Choice


class DocumentForm(forms.Form):
    docfile = forms.ImageField(
        label='Select a file'
    )
    tag = forms.CharField(label='Image tag ', max_length=100)

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

