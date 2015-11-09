from django.shortcuts import render

# Create your views here.
def index(request):
    '''
    This is the index views.
    '''
    # name : href
    links = {'Home':'/home',
			 'Contact':'/contact',
			 'About':'/about',
			 'Help':'/help',}
    return render(request, 'index.html',{'links': links})

def help(request):
    '''
    This is the help view.
    '''
    return render(request, 'help.html')
