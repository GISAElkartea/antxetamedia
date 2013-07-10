from django import forms

from multimedia.models import Account

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
