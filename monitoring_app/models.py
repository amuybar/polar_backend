from django.conf import settings
from django.db import models

class HealthData(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blood_sugar_level = models.DecimalField(max_digits=5, decimal_places=2)
    blood_pressure = models.CharField(max_length=20)
    recorded_at = models.DateTimeField(auto_now_add=True)
