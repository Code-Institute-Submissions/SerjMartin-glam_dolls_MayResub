from django.shortcuts import render
from .models import Treatment

def all_treatments(request):
    """A view to show all treatments"""

    treatments = Treatment.objects.all()

    context = {
        'treatments': treatments,
    }

    return render(request, 'treatments/treatments.html', context)

def eye_care(request):
    """A view to return the eye_care view"""

    treatments = Treatment.objects.all()

    context = {
        'treatments': treatments,
    }

    return render(request, 'treatments/eye_care.html')
