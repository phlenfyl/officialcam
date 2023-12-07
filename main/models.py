from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _

from taggit.managers import TaggableManager
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField
# Create your models here.

class Mfm(models.Model):
    desc = RichTextField(_('about'), null=True, blank=True)

    def __str__(self):
        return self.desc
    
    class Meta:
        verbose_name_plural = _("Mfm")

class WeekService(models.Model):
    name = models.CharField(_('name'), max_length = 255, null= True, blank=True)
    slug = models.SlugField(_('slug'), unique = True, blank=True, null=True)
    img = models.ImageField(_('img'), upload_to='weekly',
    default='', null = True, blank= True
    )
    image = CloudinaryField(_('Image'), overwrite= True, format= 'jpg', blank=True, null=True)
    time = models.CharField(_('time'), max_length=50,null= True, blank=True)
    display = models.BooleanField(default=False, help_text=_('To be displayed at program page'))  
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)

    tags = TaggableManager(_('tags'), blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse ('', kwargs=(self.slug))
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = _("Week Service")


class Contact(models.Model):
    fullname = models.CharField(_('fullame'), max_length=100, null=True, blank=True)
    number = models.CharField(_('number'), max_length=15, null=True, blank=True)
    email = models.EmailField(_('email'), null=True, blank=True)
    message = models.TextField(_('message'), null=True, blank=True)

    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)

    def __str__(self):
        return self.fullname
    
    class Meta:
       verbose_name_plural = _("Contact") 




# django-admin compilemessages --ignore=env
# django-admin makemessages --all --ignore=env

