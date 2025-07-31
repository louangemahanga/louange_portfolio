# portfolio/admin.py
from django.contrib import admin
from .models import Competence, Projet, ContactMessage # Importez tous vos modèles

# Enregistrez le modèle Competence
@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    # Vous pouvez personnaliser l'affichage dans l'admin ici
    list_display = ('nom', 'categorie')
    list_filter = ('categorie',)
    search_fields = ('nom',)

# Enregistrez le modèle Projet
@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_creation', 'est_mis_en_avant')
    list_filter = ('est_mis_en_avant', 'date_creation')
    search_fields = ('titre', 'description', 'technologies_utilisee')
    date_hierarchy = 'date_creation' # Si vous voulez la hiérarchie de date, assurez-vous que les données sont bonnes

# Enregistrez le modèle ContactMessage
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'date_sent')
    list_filter = ('date_sent',)
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('date_sent',) # Les messages de contact ne devraient pas être modifiés après envoi