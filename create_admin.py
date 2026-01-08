import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'opportunités.settings'  # ou 'tchad_opportunites.settings' si c'est le nom

import django
django.setup()

from django.contrib.auth.models import User

username = 'frederic2026'
email = 'fredmbaiamne@gmail.com'
password = 'TchadOpportunites2026!'  # Change ce mot de passe si tu veux un autre

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f"Superuser {username} créé avec succès !")
else:
    print(f"L'utilisateur {username} existe déjà.")
