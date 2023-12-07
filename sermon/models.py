from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from .address import Address


from taggit.managers import TaggableManager
from cloudinary.models import CloudinaryField

# Create your models here.

class Author(models.Model):
    name = models.CharField(_('name'), max_length = 100, null= True, blank=True)
    slug = models.SlugField(_('slug'), unique = True, blank=True, null=True)

    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
        
    class Meta:
        verbose_name_plural = _("Author")


class Sermon(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(_('title'), max_length = 255, null= True, blank=True)
    slug = models.SlugField(_('slug'), unique = True, blank=True, null=True)
    img = models.ImageField(_('img'), upload_to='sermon',
    default='', null = True, blank= True
    )
    image = CloudinaryField(_('image'), overwrite= True, format= 'jpg', blank=True, null=True)
    audio = models.FileField(_('audio'), upload_to= 'audio', null= True, blank=True)


    like = models.ManyToManyField(Address, related_name= 'likes', blank=True)
    like_count = models.BigIntegerField(_('like_count'), default = 0, null= True, blank=True)
    
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)

    tags = TaggableManager(_('tags'), blank=True)

    def __str__(self):
        return f"{self.author.name} - {self.title}"
    
    def get_absolute_url(self):
        return reverse ('', kwargs=(self.slug))
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = _("Sermon")

