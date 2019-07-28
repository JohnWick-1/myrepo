from django.db import models

# Create your models here.

class Laptop(models.Model):
    owner_name=models.CharField(max_length=22)
    p_date=models.DateField()
    prize=models.IntegerField()
    available=models.BooleanField()

    class Meta:
        db_table = 'Laptop_info'

    def __str__(self):
        return self.owner_name
