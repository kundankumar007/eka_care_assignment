from random import choices
from django.db import models

class concept_type(models.Model):
    
   
    id = models.BigAutoField(primary_key = True)
    concept_type_name = models.CharField(max_length = 50,blank = False)
    def __str__(self):
        return self.concept_type_name

class doctor(models.Model):
     id = models.IntegerField(primary_key = True)
     name = models.CharField(max_length = 30 ,blank = False)
     def __str__(self):
        return self.name


class concept(models.Model):

    name = models.CharField(max_length = 30 ,blank = False)
    concept_type = models.ForeignKey(concept_type, on_delete=models.CASCADE)
    doctors_name = models.ForeignKey(doctor, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    modified_at = models.DateField (auto_now = True)
    def __str__(self):
        return self.name
    








# Create your models here.
