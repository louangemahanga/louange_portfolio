# portfolio/management/commands/fix_project_dates.py
from django.core.management.base import BaseCommand
from portfolio.models import Projet
from django.utils import timezone
from django.db import transaction # Importez transaction pour une opération atomique

class Command(BaseCommand):
    help = 'Corrige les champs date_creation NULL dans le modèle Projet en les définissant à l\'heure actuelle.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Démarrage de la correction des dates de projet...'))

        try:
            # Utilisez une transaction atomique pour garantir que toutes les modifications réussissent ou échouent ensemble
            with transaction.atomic():
                # Récupère les projets dont date_creation est NULL
                projets_a_corriger = Projet.objects.filter(date_creation__isnull=True)
                count = projets_a_corriger.count()

                if count == 0:
                    self.stdout.write(self.style.SUCCESS('Aucun projet sans date_creation trouvé. Tout est en ordre !'))
                    return # Quitte si rien n'est à faire

                self.stdout.write(self.style.WARNING(f'Trouvé {count} projets avec date_creation manquante. Correction en cours...'))

                for projet in projets_a_corriger:
                    projet.date_creation = timezone.now() # Définit la date à l'heure actuelle
                    projet.save() # Sauvegarde le projet mis à jour
                    self.stdout.write(f'  Projet corrigé : "{projet.titre}" (ID : {projet.id})')

                self.stdout.write(self.style.SUCCESS(f'Mise à jour réussie de {count} projets.'))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Une erreur est survenue : {e}'))
            raise # Relance l'exception pour voir la trace complète si nécessaire