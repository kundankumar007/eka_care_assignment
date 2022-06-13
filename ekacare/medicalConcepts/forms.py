from random import choices
from django import forms



class fromClass(forms.Form):
    contentTypeChoices = [
        ('diagnosis','Diagnosis'),
        ('symptom','Symptom'),
        ('medication','Medication'),
        ('lab test', 'Lab test'),
    ]


    name = forms.CharField()
    concept_type =forms.ChoiceField(choices=contentTypeChoices)
    doctor_name = forms.CharField()

