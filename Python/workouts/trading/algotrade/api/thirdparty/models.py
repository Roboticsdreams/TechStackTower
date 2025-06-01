from django.db import models
from django.utils import timezone

class MyModel(models.Model):
    # Define your fields (example fields shown)
    token = models.IntegerField(unique=True)
    symbol = models.CharField(max_length=255,unique=True)
    stock_name = models.CharField(max_length=255)
    exchange = models.CharField(max_length=255)
    
    # Soft delete field
    deleted_at = models.DateTimeField(null=True, blank=True)

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.save()
