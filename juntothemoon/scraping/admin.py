from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin

from .models import City, ProgrammingLanguage, Vacancies


class VacancyAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Vacancies
        fields = '__all__'


class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class ProgrammingLanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class VacancyAdmin(admin.ModelAdmin):
    form = VacancyAdminForm
    list_display = ('id', 'title', 'city', 'description', 'Proglanguage', 'timestamp')
    list_display_links = ('id', 'title',)
    search_fields = ('id', 'title', 'city', 'description', 'Proglanguage', 'timestamp')



admin.site.register(City, CityAdmin)
admin.site.register(ProgrammingLanguage, ProgrammingLanguageAdmin)
admin.site.register(Vacancies, VacancyAdmin)
