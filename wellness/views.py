from django.shortcuts import render
from django.views.generic.list import ListView
from django.http import HttpResponse
from .models import Wellness



class WellnessListView(ListView):
    model = Wellness
    def get(self,request):
        wellness = self.get_queryset().all()
        context = {
            'wellness': wellness
    }
        return render(request,'wellness/index.html', context)

# def detail_view(rquest):
#     context:

#     return render(request,'detail.html',context)
