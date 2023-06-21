from django.contrib import admin

# Register your models here.

from .models import pessoa

class PessoaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'email',
        'nome',
        
    ]
    list_display_links = [
        'id',
        'nome',
    ]
   
    search_fields = [
        'nome',
        'email',
    ]

    list_editable = [
        'email',
    ]
admin.site.register(pessoa, PessoaAdmin)