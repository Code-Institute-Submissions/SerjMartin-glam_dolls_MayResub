from django.shortcuts import render
from .models import Treatment

def all_treatments(request):
    """A view to show all treatments"""

    treatments = Treatment.objects.all()

    context = {
        'treatments': treatments,
    }

    return render(request, 'treatments/treatments.html', context)
