from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    title = models.CharField(max_length=255, verbose_name="Titre de l'offre")
    description = models.TextField(verbose_name="Description")
    organization = models.CharField(max_length=200, verbose_name="Organisation / Entreprise")
    city = models.CharField(max_length=100, verbose_name="Ville", blank=True)
    deadline = models.DateField(verbose_name="Date limite", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

class Opportunity(models.Model):
    title = models.CharField(max_length=255, verbose_name="Titre")
    description = models.TextField(verbose_name="Description")
    type_opp = models.CharField(max_length=100, verbose_name="Type (Formation, Bourse, Appel à projet)")
    organization = models.CharField(max_length=200, verbose_name="Organisateur")
    deadline = models.DateField(verbose_name="Date limite", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title