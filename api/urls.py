from . import views
from django.urls import path


from rest_framework.decorators import api_view
from rest_framework.response import Response



urlpatterns = [
    path('', views.apiInit,name="api-overview"),
]