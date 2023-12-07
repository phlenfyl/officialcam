from django.db.models import fields
from rest_framework import serializers
from program.models import *
from .models import *
from sermon.models import *


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'


class WeekServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeekService
        fields = '__all__'

class SermonSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source = 'author.name')
    audio_url = serializers.SerializerMethodField()
    class Meta:
        model = Sermon
        fields = ['id', 'title', 'slug', 'img', 'audio', 'like_count', 'created', 'updated', 'author', 'author_name', 'audio_url', 'like']
    
    def get_audio_url(self, obj):
        if obj.audio:
            return self.context['request'].build_absolute_uri(obj.audio.url)
        return None

class AuthorSerializer(serializers.ModelSerializer):
    sermon = SermonSerializer(many= True, required = False)
    class Meta:
        model = Author
        fields = '__all__'


