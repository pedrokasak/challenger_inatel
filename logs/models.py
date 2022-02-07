from django.db import models

class Error(models.Model):
    user = models.CharField(max_length=16, db_index=True, null=True, blank=True)
    category = models.CharField(max_length=64, db_index=True)
    url = models.URLField(null=True, blank=True)
    error = models.TextField(max_length=256)
    ip = models.GenericIPAddressField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category

    class Meta:
        db_table = 'logs'
        verbose_name = 'error'
        verbose_name_plural = 'errors'
