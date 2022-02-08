from django.urls import path
from .models import mode

urlpatterns = [path("hello", mode)]
