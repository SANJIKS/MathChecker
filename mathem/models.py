from django.db import models

class History(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    ip = models.CharField(max_length=120)
    data = models.TextField()
    result = models.BooleanField()