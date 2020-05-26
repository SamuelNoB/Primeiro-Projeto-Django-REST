from django.contrib import admin
from .models import Endereco
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
class EnderecosAdmin(LeafletGeoAdmin):
    pass

admin.site.register(Endereco, EnderecosAdmin)