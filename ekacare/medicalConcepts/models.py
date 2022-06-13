from random import choices
from django.db import models


class concept(models.Model):
    contentTypeChoices = [
        ('diagnosis','Diagnosis'),
        ('symptom','Symptom'),
        ('medication','Medication'),
        ('lab test', 'Lab test'),
        ]
    name = models.CharField(max_length = 30 ,blank = False)
    concept_type = models.CharField(max_length = 50,blank = False,choices = contentTypeChoices,default = 'diagnosis')
    doctors_name = models.CharField(max_length = 30,blank = False)
    created_at = models.DateTimeField(auto_now_add = True)
    modified_at = models.DateField (auto_now = True)
    def __str__(self):
        return self.name

class doctor(models.Model):
     id = models.IntegerField(primary_key = True)
     name = models.CharField(max_length = 30 ,blank = False)
     def __str__(self):
        return self.name

class concept_type(models.Model):
    contentTypeChoices = [
        ('diagnosis','Diagnosis'),
        ('symptom','Symptom'),
        ('medication','Medication'),
        ('lab test', 'Lab test'),
    ]
   
    id = models.BigAutoField(primary_key = True)
    concept_type_name = models.CharField(max_length = 50,blank = False,choices = contentTypeChoices,default = 'diagnosis')
    def __str__(self):
        return self.concept_type_name





# Create your models here.
