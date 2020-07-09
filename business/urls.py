from django.urls import path
from business.views import BusinessListView

from . import views

urlpatterns = [
    path('', BusinessListView.as_view(), name='business-index'),
]