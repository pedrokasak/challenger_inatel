from django.db import models


class ImportsFile(models.Model):

    archive = models.FileField(
        verbose_name='Arquivo', upload_to='imports/%m/%Y/', null=True, blank=True)

    def __str__(self):
        return self.archive

    class Meta:
        verbose_name = 'arquivo'
        verbose_name_plural = 'arquivos'
