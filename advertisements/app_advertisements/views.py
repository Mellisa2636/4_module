from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    advertesements = Advertisement.objects.all()
    context = { 'advertisements' : advertisements}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')