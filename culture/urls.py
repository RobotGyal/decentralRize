from django.urls import path
from culture.views import CultureListView

from . import views

urlpatterns = [
    path('', CultureListView.as_view(), name='culture-index'),
]