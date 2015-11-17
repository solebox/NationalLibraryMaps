from django.shortcuts import render
from djgeojson.views import GeoJSONLayerView

class MapLayer(GeoJSONLayerView):
    bbox_auto = True
    # Options
   # precision = 4   # float
   # simplify = 0.5  # generalization
    srid = 26918

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
