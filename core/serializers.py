from django.conf import settings
from django.db import models
from django.db.models import fields
from django.db.models.query import QuerySet
from rest_framework import serializers

from core.models import Content,Tag

class ContentSerializer(serializers.ModelSerializer):
    text_title  =   serializers.CharField(max_length=255)
    class Meta:
        model = Content
        fields = '__all__'
    

    def create(self,validated_data):
        title = validated_data.get('text_title',None)
        # __iexact
        validated_data['text_title'],status =Tag.objects.get_or_create(title  = title)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        title = validated_data.get('text_title',None)
        # __iexact
        validated_data['text_title'],status =Tag.objects.get_or_create(title  = title)
        return super().update(instance, validated_data)

class ContentListSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Content
        fields = ('id','url')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
             