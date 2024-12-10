from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pokemon(models.Model):
    poke_type=models.CharField(max_length=200)
    poke_name=models.CharField(max_length=200)
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="pokemon")
 