from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Название города")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    class Meta:
        verbose_name = "Название города"
        verbose_name_plural = "Название города"
        ordering = ['-name']

    def __str__(self):
        return self.name


class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Язык программирования")
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name="URL")

    class Meta:
        verbose_name = "Язык программирования"
        verbose_name_plural = "Язык программирования"

    def __str__(self):
        return self.name


class Vacancies(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=255, verbose_name="Вакансия")
    company = models.CharField(max_length=255, verbose_name="Название компании")
    description = models.TextField(verbose_name="Описание вакансии")
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name="Город")
    Proglanguage = models.ForeignKey('ProgrammingLanguage', on_delete=models.CASCADE, verbose_name="Язык программирования")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата опубликования")


    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"

    def __str__(self):
        return self.title

