from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^resumes/$', views.ResumeList.as_view(), name='resume-list'),
    url(r'^insert/$', views.InsertResume.as_view(), name='insert-resume'),
    url(r'^update/(?P<pk>\d+)/$', views.UpdateResume.as_view(), name='update-resume'),


]
