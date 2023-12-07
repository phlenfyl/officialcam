from django.db import models
from django.utils.translation import gettext_lazy as _

class Address(models.Model):

    ip = models.CharField(_('ip address'), max_length=40, unique=True, default = '0.0.0.0', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Address"

    def __str__(self):
        return self.ip