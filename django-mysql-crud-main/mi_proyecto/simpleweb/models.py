from django.db import models

# Create your models here.
class MiModelo(models.Model):
    campo1 = models.CharField(max_length=100)
    campo2 = models.IntegerField()
    campo3 = models.BooleanField(default=False)

    def __str__(self):
        return self.campo1