# portfolio/views.py

from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
# from django.templatetags.static import static # <-- TRÈS IMPORTANT : Supprimez cette ligne !

from .models import Competence, Projet # Assurez-vous d'importer ContactMessage si vous le gérez via un modèle

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if not all([name, email, subject, message]):
            messages.error(request, 'Veuillez remplir tous les champs du formulaire avant d\'envoyer.')
        else:
            try:
                send_mail(
                    f'Message de contact de {name}: {subject}',
                    f'De: {name}\nEmail: {email}\n\nMessage:\n{message}',
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.RECIPIENT_ADDRESS], # Assurez-vous que RECIPIENT_ADDRESS est défini dans settings.py
                    fail_silently=False,
                )
                messages.success(request, 'Votre message a été envoyé avec succès ! Je vous répondrai très bientôt.')
                return HttpResponseRedirect(reverse('home') + '#contact')
            except Exception as e:
                messages.error(request, f'Désolé, une erreur est survenue lors de l\'envoi de votre message : {e}')

    competences = Competence.objects.all().order_by('categorie', 'nom')
    projets = Projet.objects.all().order_by('-date_creation')

    context = {
        'competences': competences,
        'projets': projets,
        'whatsapp_number': '242069905134',
        # 'email_address': 'louangemahanga757@gmail.com',
        # --- CORRECTION ICI POUR LE CV ---
        # Le chemin est une simple chaîne de caractères, le template s'occupera du reste.
        # ATTENTION AU CARACTÈRE 'é' : Renommez si possible en 'sacre_louange.pdf'
        # pour éviter les problèmes d'encodage sur certains serveurs.
        'cv_url': 'docs/louange.pdf',
        
        # --- VOS VRAIES URLS ICI ---
        'linkedin_url': 'https://www.linkedin.com/in/sacr%C3%A9-louange-mahanga-tsona/',
        'github_url': 'https://github.com/louangemahanga', # Ceci pointe vers un projet, pas un profil général. Assurez-vous que c'est ce que vous voulez.
        'facebook_url': 'https://www.facebook.com/MAHANGA_TSONA_sacré_louange', # Assurez-vous que c'est une URL de profil/page valide.
    }
    return render(request, 'index.html', context)

def project_detail(request, pk):
    projet = get_object_or_404(Projet, pk=pk)
    return render(request, 'project_detail.html', {'projet': projet})