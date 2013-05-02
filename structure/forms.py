from django import forms

from structure.models import Node


class NodeForm(forms.ModelForm):
    class Meta:
        model = Node

    def __init__(self, *args, **kwargs):
        super(NodeForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['parent'].queryset = Node.objects.exclude(
                    pk=self.instance.pk)
