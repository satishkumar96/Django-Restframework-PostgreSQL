from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField("Name", max_length=200)
    email = models.EmailField()
    created = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.name