from django.contrib import admin
from testapp.models import movie
# Register your models here.
class movie_Admin(admin.ModelAdmin):

    list_display=['rdate','moviename','hero','heroin','rating']

admin.site.register(movie,movie_Admin)
