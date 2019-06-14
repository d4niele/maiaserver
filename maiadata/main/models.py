from django.db import models

class Data(models.Model):
    espid = models.CharField(max_length=20)
    topic = models.CharField(max_length=15,default="")
    timestamp = models.PositiveIntegerField()
    peso = models.PositiveIntegerField()
    temperatura = models.PositiveIntegerField()
    umidita = models.PositiveIntegerField()

    class Meta:
        verbose_name = "record"
        verbose_name_plural = "records"