from django import forms

from antxetamedia.multimedia.models import Account

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
