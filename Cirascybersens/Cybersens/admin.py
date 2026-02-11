from django.contrib import admin
from django.utils.html import format_html
from .models import CyberHygiene

admin.site.site_header = "Administration CyberSécurité"
admin.site.site_title = "Portail CyberHygiène"
admin.site.index_title = "Bienvenue sur votre gestionnaire de contenu"

# Register your models here.
@admin.register(CyberHygiene)
class CyberHygieneAdmin(admin.ModelAdmin):
    list_display = ('titre', 'categorie', 'date_pub', 'image')
    list_filter = ('categorie', 'date_pub')
    search_fields = ('titre', 'description')

    fieldsets = (
        ('Informations principales', {
            'fields': ('titre', 'slug', 'categorie')
        }),
        ('Contenu visuel et texte', {
            'fields': ('image', 'description'),
        }),
    )



    def aperçu_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: auto; border-radius: 5px;" />', obj.image.url)
        return "Pas d'image"
    
    # On remplace allow_tags par format_html ci-dessus
    aperçu_image.short_description = 'Aperçu'