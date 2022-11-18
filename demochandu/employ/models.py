from django.db import models
from django.urls import reverse


__all__ = (
    'Employ',
)


class Employ(models.Model):
    
    
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    first_name = models.CharField(
        max_length=100,
        unique=True
    )
    last_name = models.CharField(
        max_length=100,
        unique=True
    )
    date_of_birth = models.DateField()
    gender = models.CharField(
        max_length=1, 
        choices=GENDER_CHOICES
    )
    
    
    class Meta:
        ordering = ['first_name']

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse("employ:employtype", kwargs={"pk": self.pk})

   

