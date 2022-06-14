from . import models
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm

class EditeurForms(ModelForm):
    class Meta:
        models = models.Editeur
        fields = {'nom', 'date', 'logo'}
        labels = {'nom': _('Nom'),
                  'date': _('Date de creation'),
                  'logo': _('URL de l\'image'),
                  }

class CategorieForms(ModelForm):
    class Meta:
        models = models.Categorie
        fields = {'nom', 'description'}
        labels = {
            'nom': _('Nom de la catégorie'),
            'description': _('Description de la catégorie'),
        }

class CommentaireForms(ModelForm):
    class Meta:
        models = models.Commentaire
        fields = {'jeux', 'joueur', 'note', 'commentaire', 'date'}
        labels = {'jeux': _('Jeux'),
                  'joueur': _('Joueur'),
                  'note': _('Note'),
                  'commentaire': _('Commentaire'),
                  'date': _('Date'),
                  }

class JeuxForms(ModelForm):
    class Meta:
        models = models.Jeux
        fields = {'titre', 'date_sortie', 'photo'}
        labels = {
            'titre': _('Titre'),
            'date_sortie': _('Date de sortie'),
            'photo': _('URL de l\'image'),
        }

class JoueurForms(ModelForm):
    class Meta:
        models = models.Joueur
        fields = {'nom', 'prenom', 'mail', 'mdp', 'type'}
        labels = {
            'nom': _('Nom'),
            'prenom': _('Prenom'),
            'mail': _('Adresse mail'),
            'mdp': _('Mot de passe'),
            'type': _('Type de profil'),
        }