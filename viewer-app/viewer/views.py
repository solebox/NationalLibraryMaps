from django.shortcuts import render
from viewer.models import MyMaps
from django.http import JsonResponse

links = {'Home':'/home', 'Contact':'/contact',
         'About':'/about', 'Help':'/help',}

def index(request):
    '''
    This is the index views.
    '''
    return render(request, 'index.html', {'links': links})

def help(request):
    '''
    This is the help view.
    '''
    return render(request, 'help.html', {'links': links})

def privacyAndTerms(request):
    '''

    :param request:
    :return:
    '''
    return render(request, 'privacyAndTerms.html', {'links': links})


def getAllMaps(request):
    my_maps = MyMaps.objects.all()


    return JsonResponse([{
        'id': map.id,
        'url': 'http://localhost:3000/maps/tile/' + map.id + '/{z}/{x}/{y}.png',
    } for map in my_maps], safe=False)