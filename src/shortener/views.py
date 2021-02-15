from django.shortcuts import render, redirect
import uuid
from .models import Url
from django.http import  HttpResponse

def index(request):
    return render(request, 'url/index.html')

def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        unique_identifier = str(uuid.uuid4())[:5]
        url = Url(link=link, uuid=unique_identifier)
        url.save()
        return HttpResponse(unique_identifier)

def go(request, pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect(url_details.link)