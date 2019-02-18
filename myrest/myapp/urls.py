from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^resumes/$', views.ResumeList.as_view(), name='resume-list'),

]
