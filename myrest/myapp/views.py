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


# Create your views here.

class ResumeList(generics.ListCreateAPIView):

    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [Or(IsAdminUser, TokenHasReadWriteScope)]

