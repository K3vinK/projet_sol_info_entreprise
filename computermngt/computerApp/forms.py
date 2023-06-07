from django import forms
from django . core . exceptions import ValidationError
from .models import Machine


class AddMachineForm(forms.Form):

    nom = forms.CharField(required=True, label='Nom de la machine')

    def clean_nom(self):
        data = self.cleaned_data['nom']
        if len(data) != 6:
            raise ValidationError("Erreur de format pour le champ nom")

        return data

class DelMachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = []  # No fields are required for the deletion form

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['machine_id'] = forms.ModelChoiceField(queryset=Machine.objects.all(), empty_label=None, label='Machine')

    def delete_machine(self):
        machine = self.cleaned_data.get('machine_id')
        machine.delete()

