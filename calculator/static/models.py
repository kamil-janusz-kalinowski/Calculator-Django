from django.db import models

class Calculation(models.Model):
    expression = models.CharField(max_length=255)
    result = models.FloatField()
    calculated_at = models.DateTimeField(auto_now_add=True)