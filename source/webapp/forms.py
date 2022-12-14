from django import forms
from django.forms import widgets


class GuestsListForm(forms.Form):
    author = forms.CharField(max_length=200, required=True, label='Name:')
    email = forms.EmailField(max_length=200, required=True, label='Email:')
    content = forms.CharField(max_length=3000,
                              required=True,
                              label='Text:',
                              widget=widgets.Textarea(attrs={"cols": 50, "rows": 5}))


class GuestSearchForm(forms.Form):
    author = forms.CharField(max_length=200, required=True, label='Name')
