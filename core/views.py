from django.http import request
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import serializers, status, exceptions,authentication,generics,viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.models import Content, Tag
from core.serializers import ContentSerializer,TagSerializer,ContentListSerializer
# Create your views here.

# for CURD operation of Conetent
class ContentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Content.objects.all()
    serializer_class = ContentSerializer        
    
    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user)
        return queryset
    # custom list function
    def list(self,request,*args,**kwargs):
        custom_data = {
            'count_of_items' : self.get_queryset().count(),
            'list_of_items': ContentListSerializer(self.get_queryset(),many=True,context={'request': request}).data,  # this is the default result you are getting today
        }
        return Response(custom_data)
 
# Tag listing and retrieving details
class TagViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        details = Content.objects.filter(text_title__id = pk)
        serializer = ContentSerializer(details,many=True,context={'request': request})
        return Response(serializer.data)