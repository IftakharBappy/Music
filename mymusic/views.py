from django.shortcuts import render
from django.http import HttpResponse
from .models import Album
from django.template import loader


def index(request):
    all_albums = Album.objects.all()
    templete = loader.get_template('music/index.html')
    context = {
        'all_albums': all_albums,
    }
    return HttpResponse(templete.render(context, request))
