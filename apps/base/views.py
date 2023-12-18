from django.shortcuts import render
from apps.base import models

# Create your views here.
def index(request):
    settings = models.Settings.objects.latest('id')
    skils = models.Skils.objects.all()
    services = models.Services.objects.all()
    projects = models.Projects.objects.all()
    rewievs = models.Rewievs.objects.all()
    contacts = models.Contacts.objects.latest('id')
    portfolio = models.Portfolio.objects.all()

    return render(request,'index.html', locals())