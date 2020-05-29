from django.urls import path
from . import views

app_name = 'rel_app'

urlpatterns=[
    path('relative/',views.relative,name='relative'),
    path('another/',views.another,name = 'another'),
]
