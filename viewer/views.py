from django.shortcuts import render

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
