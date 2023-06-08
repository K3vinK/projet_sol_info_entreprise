from django import forms
from django . core . exceptions import ValidationError
from .models import Machine, Personne


class AddMachineForm(forms.Form):

    nom = forms.CharField(required=True, label='Nom de la machine')

    def clean_nom(self):
        data = self.cleaned_data['nom']
        if len(data) != 6:
            raise ValidationError("Erreur de format pour le champ nom")

        return data

class DelMachineForm(forms.ModelForm):
    class Meta:
        model = Machine  # Specify the model class associated with the form
        fields = ['machine_id']  # Specify the fields you want to include in the form

    machine_id = forms.ModelChoiceField(queryset=Machine.objects.all(), label="Select Machine") #label permet de changer des noms

    def delete_machine(self):
        machine = self.cleaned_data.get('machine_id')
        if machine:
            machine.delete()

class DelPersonneForm(forms.ModelForm):
    class Meta:
        model = Personne
        fields = ['personne_id']

    personne_id = forms.ModelChoiceField(queryset=Personne.objects.all(), label="Select Person")

    def delete_personne(self):
        personne = self.cleaned_data.get('personne_id')
        if personne:
            personne.delete()
