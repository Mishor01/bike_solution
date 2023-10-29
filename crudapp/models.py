from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=150, verbose_name="Name")
    username = models.CharField(max_length=150, verbose_name="Username")
    email = models.EmailField(max_length=277, verbose_name="User Email")

    def __str__(self):
        return str(self.id)