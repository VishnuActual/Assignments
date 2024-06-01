# forms.py
from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields ='__all__'


class MovieSearchForm(forms.Form):
    query = forms.CharField(label='Search')
