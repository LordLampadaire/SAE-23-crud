from django.forms import ModelForm
from . import models
from django.utils.translation import gettext_lazy as _
from django.forms.widgets import NumberInput
from django import forms

class EditeurForm(ModelForm):
    class Meta:
        model = models.Editeur
        fields = {'nom', 'date', 'logo'}
        labels = {'nom': _('Nom'),
                  'date': _('Date de creation'),
                  'logo': _('URL de l\'image'),
                  }

class CategorieForm(ModelForm):
    class Meta:
        model = models.Categorie
        fields = {'nom', 'description'}
        labels = {
            'nom': _('Nom de la categorie'),
            'description': _('Description de la categorie'),
        }

class CommentaireForm(ModelForm):
    class Meta:
        model = models.Commentaire
        fields = {'jeux', 'joueur', 'note', 'commentaire', 'date'}
        labels = {'jeux': _('Jeux'),
                  'joueur': _('Joueur'),
                  'note': _('Note'),
                  'commentaire': _('Commentaire'),
                  'date': _('Date'),
                  }

class JeuxForm(ModelForm):
    class Meta:
        model = models.Jeux
        fields = {'titre', 'date_sortie'}
        labels = {
            'titre': _('Titre'),
            'date_sortie': _('Date de sortie'),
        }

class JoueurForm(ModelForm):
    class Meta:
        model = models.Joueur
        fields = {'nom', 'prenom', 'mail', 'mdp', 'type'}
        labels = {
            'nom': _('Nom'),
            'prenom': _('Prenom'),
            'mail': _('Adresse mail'),
            'mdp': _('Mot de passe'),
            'type': _('Type de profil'),
        }