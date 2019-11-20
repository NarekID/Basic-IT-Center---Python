from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=40)
    year = models.DecimalField(decimal_places=0, max_digits=4)
    mog = models.DecimalField(decimal_places=2, max_digits=5)
    
    def __str__(self):
        return self.surname + ' ' + self.name
    
    class Meta:
        ordering = ('surname',
                    'name',
                    'mog',)
