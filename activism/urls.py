from django.urls import path
from activism.views import ActivismListView

from . import views

urlpatterns = [
    path('', ActivismListView.as_view(), name='activism-index'),
]