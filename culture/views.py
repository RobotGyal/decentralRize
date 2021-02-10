from django.shortcuts import render
from django.views.generic.list import ListView
from django.http import HttpResponse
from .models import Culture



class CultureListView(ListView):
    model = Culture
    def get(self,request):
        culture = self.get_queryset().all()
        context = {
            'culture': culture
        }
        return render(request,'culture/index.html', context)