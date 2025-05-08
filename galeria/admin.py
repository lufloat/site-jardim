from django.contrib import admin
from galeria.models import jardins
from django.db import models

class Listandojardins(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "publicada" )
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_per_page = 10
    list_editable = ("publicada",)
    publicada = models.BooleanField(default=False)


admin.site.register(jardins, Listandojardins)