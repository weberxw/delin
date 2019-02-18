# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Music
from .serializers import MusicSerializer
from rest_framework import generics



# Create your views here.

class MusicList(generics.ListCreateAPIView):

    queryset = Music.objects.all()
    serializer_class = MusicSerializer

