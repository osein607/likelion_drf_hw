from rest_framework import serializers
from .models import *

class SingerImageSerializer(serializers.ModelSerializer):
  class Meta:
    model = SingerImage
    fields = ['id', 'image']

class SingerSerializer(serializers.ModelSerializer):
  id = serializers.CharField(read_only=True)
  songs = serializers.SerializerMethodField(read_only=True)
  images = SingerImageSerializer(many=True, read_only=True)
  # use_url=True, required=False

  def get_songs(self, instance):
    serializer = SongSerializer(instance.songs, many=True)
    return serializer.data

  tags = serializers.SerializerMethodField()

  def get_tags(self, instance):
    tag = instance.tags.all()
    return [t.name for t in tag]

  class Meta:
    model = Singer
    fields = '__all__'
    
class SongSerializer(serializers.ModelSerializer):
  class Meta:
    model = Song
    fields = '__all__'
    read_only_fields = ['singer']

class TagSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tag
    fields = '__all__'