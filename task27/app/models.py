from django.db import models

# Create your models here.
class cpu_ram_model(models.Model):
    cpu_percentage=models.FloatField()
    ram_percentage=models.FloatField()
    date=models.DateTimeField(auto_now=True)
