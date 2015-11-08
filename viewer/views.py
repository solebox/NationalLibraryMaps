from django.shortcuts import render

# Create your views here.
def index(request):
    '''
    This is the index views.
    '''
    return render(request, 'index.html')

def help(request):
    '''
    This is the help view.
    '''
    return render(request, 'help.html')
