from django.db import models

class Data(models.Model):
    espid = models.CharField(max_length=20)
    topic = models.CharField(max_length=15,default="")
    timereg = models.DateTimeField(null=True,blank=True)
    timestamp = models.PositiveIntegerField()
    peso = models.FloatField()
    temperatura = models.FloatField()
    umidita = models.FloatField(verbose_name="umidità")

    class Meta:
        verbose_name = "record"
        verbose_name_plural = "records"