from rest_framework import serializers
from .models import Resume
from myapp.models import Myrest
from django.contrib.auth.models import User

class ResumeSerializer(serializers.ModelSerializer):

    class Meta:

        model = Resume
        fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

class MyrestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Myrest
        fields = ('id', 'description','done')