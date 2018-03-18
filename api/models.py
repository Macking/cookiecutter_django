from django.db import models

# Create your models here.


class Api(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ('name', )
