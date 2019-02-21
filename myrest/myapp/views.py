# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Resume
from .serializers import ResumeSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_condition import Or
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope, OAuth2Authentication
from rest_framework.authentication import SessionAuthentication
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
from myapp.permissions import CustomObjectPermissions



# Create your views here.

class ResumeList(generics.ListAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = (CustomObjectPermissions,)
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = '__all__'
    ordering_fields = '__all__'
    ordering = ('id',)

class InsertResume(generics.CreateAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = (CustomObjectPermissions,)



class UpdateResume(generics.UpdateAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = (CustomObjectPermissions,)
    

