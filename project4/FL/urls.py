from django.urls import path

from .views import ursafe

urlpatterns = [
    path('', ursafe),
]
