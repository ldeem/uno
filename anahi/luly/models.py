from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Usuario(models.Model):
		"""docstring for telefono """
		id_persona = models.OneToOneField(User,related_name='id_persona')
		sexo = models.BooleanField(default=True)