from django.shortcuts import render
from django.views.generic.list import ListView
from django.http import HttpResponse
from .models import Business



class BusinessListView(ListView):
    model = Business
    def get(self,request):
        business = self.get_queryset().all()
        context = {
            'business': business
        }
        return render(request,'business/index.html', context)
