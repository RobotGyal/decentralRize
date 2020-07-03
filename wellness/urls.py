from django.urls import path 
from wellness.views import WellnessListView
from . import views

urlpatterns = [
    path('', WellnessListView.as_view(), name='wellness-list-page'),
]