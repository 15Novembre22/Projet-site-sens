from django.contrib import admin
from .models import Incident
# Register your models here.
@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ('type_incident', 'description', 'email_contact', 'capture_ecran')
    list_filter = ('date_signalement', 'type_incident')
    search_fields = ('type_incident', 'description')

    fieldsets = (
        ('Informations principales', {
            'fields': ('type_incident','email_contact')
        }),
        ('Contenu visuel et texte', {
            'fields': ('capture_ecran', 'description'),
        }),
    )
