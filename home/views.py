from django.shortcuts import render


# Create your views here.

def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


def page_not_found_view(request, *args, **kwargs):
    
    return render(request, 'home/404.html', status=404)


def faq(request):

    return render(request, 'home/faq.html')