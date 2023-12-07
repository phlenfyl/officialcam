from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from .address import Address


from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
from embed_video.fields import EmbedVideoField
from cloudinary.models import CloudinaryField

# Create your models here.

class Program(models.Model):
    title = models.CharField(_('title'), max_length = 255, null= True, blank=True)
    slug = models.SlugField(_('slug'), unique = True, blank=True, null=True)
    desc = RichTextField(_('desc'), null= True, blank=True)
    img = models.ImageField(_('img'), upload_to='program',
    default='', null = True, blank= True
    )
    image = CloudinaryField(_('image'), overwrite= True, format= 'jpg', blank=True, null=True)
    video = EmbedVideoField(_('video'), null= True, blank=True)


    like = models.ManyToManyField(Address, related_name= 'likes', blank=True)
    like_count = models.BigIntegerField(_('like_count'), default = 0, null= True, blank=True)

    speicalprogram= models.BooleanField(_('specialprogram'), null= True, blank=True)
    deliverance = models.BooleanField(_('deliverance'), null= True, blank=True)
    counseling = models.BooleanField(_('counseling'), null= True, blank=True)

    display = models.BooleanField(_('display'), null= True, blank=True)
    
    date = models.CharField(_('date'), max_length = 50, null= True, blank=True)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)


    tags = TaggableManager(_('tags'), blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse ('', kwargs=(self.slug))
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = _("Program")

class ProgramNum(models.Model):
    name = models.ForeignKey(Program, on_delete = models.CASCADE, related_name = 'pag')

    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = _("ProgramNum")

# class SpeialProgram(models.Model):
#     title = models.CharField(max_length = 255, null= True, blank=True)
#     slug = models.SlugField(unique = True, blank=True, null=True)
#     desc = RichTextField(null= True, blank=True)
#     img = models.ImageField(upload_to='special',
#     default='', null = True, blank= True
#     )
#     video = EmbedVideoField(null= True, blank=True)


#     like = models.ManyToManyField(Address, related_name= 'likes', blank=True)
#     like_count = models.BigIntegerField(default = 0, null= True, blank=True)
    
    
#     date = models.CharField(max_length = 50, null= True, blank=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)


#     tags = TaggableManager(blank=True)

#     def __str__(self):
#         return self.title
    
#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.title)
#         return super().save(*args, **kwargs)
    
#     class Meta:
#         verbose_name_plural = "Special Program"
