from django.urls import path
from .views import myview

urlpatterns = [
    path("hello", myview),
]
