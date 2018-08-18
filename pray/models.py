from django.db import models
from django.core.validators import validate_email

# Create your models here.
class Detail(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100,validators=[validate_email])
    mobile = models.CharField(max_length=10)
 
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.name