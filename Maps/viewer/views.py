from django.shortcuts import render

# Create your views here.
def index(request):
    '''
    this is the index views.
    '''
    return render(request, 'index.html')
