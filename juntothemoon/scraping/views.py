from django.shortcuts import render

from .models import Vacancies


def index(request):
    vacancies = Vacancies.objects.all()
    return render(request, "juntothemoon/index.html", {"vacancies": vacancies})
