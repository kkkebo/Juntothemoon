from django.shortcuts import render

from .forms import FindForm
from .models import Vacancies


def index(request):
    form = FindForm()
    city = request.GET.get('city')
    language = request.GET.get('language')
    vacancies = []
    if city or language:
        fltr = {}
        if city:
            fltr['city__slug'] = city
        if language:
            fltr['Proglanguage__slug'] = language

        vacancies = Vacancies.objects.filter(**fltr)
    return render(request, "juntothemoon/index.html", {"vacancies": vacancies, 'form': form})
