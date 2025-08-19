# portfolio/models.py
from django.db import models
from django.urls import reverse
from django.utils import timezone # IMPORTER timezone

# CATEGORIE_CHOICES est défini ici, au niveau du module
CATEGORIE_CHOICES = [
    ('Frontend', 'Frontend'),
    ('Backend', 'Backend'),
    ('Mobile', 'Mobile'),                   
    ('Base de Données', 'Base de Données'),
    ('DevOps', 'DevOps'),
    ('Outil', 'Outil'),
    ('Autre', 'Autre'),
]

class Competence(models.Model):
    nom = models.CharField(max_length=100)
    categorie = models.CharField(max_length=50, choices=CATEGORIE_CHOICES)

    class Meta:
        verbose_name_plural = "Compétences"
        ordering = ['categorie', 'nom']

    def __str__(self):
        return self.nom

class Projet(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projets/', blank=True, null=True)
    technologies_utilisee = models.CharField(max_length=255, help_text="Ex: Django, React.js, PostgreSQL")
    url_demo = models.URLField(blank=True, null=True, verbose_name="URL de la Démo")
    url_github = models.URLField(blank=True, null=True, verbose_name="URL GitHub")
    date_creation = models.DateTimeField(auto_now_add=True)
    est_mis_en_avant = models.BooleanField(default=False, verbose_name="Mettre en avant sur la page d'accueil")

    class Meta:
        # La virgule en trop a été retirée ici, c'est parfait !
        ordering = ['-date_creation'] 

    def __str__(self):
        return self.titre

    def get_absolute_url(self):
        return reverse('project_detail', args=[str(self.id)])

class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom / Organisation")
    email = models.EmailField(verbose_name="Email de l'expéditeur")
    subject = models.CharField(max_length=200, verbose_name="Sujet du message")
    message = models.TextField(verbose_name="Message")
    date_sent = models.DateTimeField(auto_now_add=True, verbose_name="Date d'envoi")

    class Meta:
        verbose_name = "Message de Contact"
        verbose_name_plural = "Messages de Contact"
        ordering = ['-date_sent']

    def __str__(self):
        return f"Message de {self.name} - Sujet: {self.subject}"