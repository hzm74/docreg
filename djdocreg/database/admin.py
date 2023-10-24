from django.contrib import admin

# Register your models here.
from .models import Vloeren
from .models import Bedrijven

admin.site.register(Vloeren)
admin.site.register(Bedrijven)

class VloerenAdmin(admin.ModelAdmin):
    list_display = ('nummer','documentnaam',)
    ordering = ('nummer',)
    search_fields = ('nummer',)

#admin.site.register(Vloeren, VloerenAdmin)

