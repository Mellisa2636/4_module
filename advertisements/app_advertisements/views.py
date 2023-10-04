from django.http import HttpResponse
from django.shortcuts import render
from .models import Advertisements
from .forms import AdvertisementForms

# Create your views here.

def index(request):
    advertesements = Advertisements.objects.all()
    context = { 'advertisements' : advertesements}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')


def adv_post(request):
    form = AdvertisementForms()
    context = {'form': form}
    return render(request, 'advertisement-post.html')