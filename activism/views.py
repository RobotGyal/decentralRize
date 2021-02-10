from django.shortcuts import render
from django.views.generic.list import ListView
from django.http import HttpResponse
from .models import Activism



class ActivismListView(ListView):
    model = Activism
    def get(self,request):
        activism = self.get_queryset().all()
        context = {
            'activism': activism
        }
        return render(request,'activism/index.html', context)