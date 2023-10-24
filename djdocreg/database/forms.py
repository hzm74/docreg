from django import forms
from django.forms import ModelForm

from .models import Bedrijven
from .models import Vloeren
from .models import Controlemomenten_gepland
from .models import Datum_Document
from .models import Projecten

from django.db.models import F, Max

from django.forms import ModelChoiceField

from itertools import chain

class ProjectenForm(ModelForm):
    class Meta:
        model = Projecten
        fields = [
            'projectnummer', 'projectnaam', 'plaats'
        ]


class BedrijvenForm(ModelForm):
    class Meta:
        model = Bedrijven
        fields = [
            'bedrijfsnaam'
        ]

class VloerenForm(ModelForm):
    class Meta:
        model = Vloeren
        fields = [
            'projectnaam', 'bedrijfsnaam', 'nummer', 'documentnaam', 'bestand'
        ]

class Datum_DocumentForm(ModelForm):
    class Meta:
        model = Datum_Document
        fields = [
            'datum', 
        ]
        widgets = {
                'datum': forms.SelectDateWidget()
                }

class Controlemomenten_geplandForm(ModelForm):
    class Meta:
        model = Controlemomenten_gepland
        fields = [
            'ter_eerste_controle_gepland',
            'ter_eerste_controle_retour_binnen_gepland',
            'ter_tweede_controle_gepland',
            'ter_tweede_controle_retour_binnen_gepland',
            'definitief_binnen_gepland',
            #'vloeren'
        ]

# class Update_documentForm(forms.Form):
#     datumnew = forms.DateField(widget=forms.SelectDateWidget)

#     vloeren = forms.ModelMultipleChoiceField(
#                     widget = forms.CheckboxSelectMultiple,
#                     queryset = Vloeren.objects.annotate(laatste=Max('datum_document__datum')).filter(datum_document__datum=F('laatste'))
#                     )


