from django.shortcuts import render, HttpResponse



def index(request):
    return render(request, 'base.html')

def pagetest(request):
    return render(request, 'page_test.html')