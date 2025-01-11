
from django.urls import path

from users.api.api import basic


urlpatterns = [
    path('api/',basic, name='api_basic' ),
]
