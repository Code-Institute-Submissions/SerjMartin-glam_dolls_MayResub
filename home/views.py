from django.shortcuts import render


def index(request):
    """A view to return the index view"""

    return render(request, 'home/index.html')
