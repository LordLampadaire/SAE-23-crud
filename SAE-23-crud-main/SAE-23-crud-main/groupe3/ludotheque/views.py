from django.shortcuts import render
from . import models, forms
from .forms import CategorieForms, JeuxForms, JoueurForms, EditeurForms, CommentaireForms, ModelForm

"""def test(request):
    return render(request, )"""


def get_categorie(request):
    liste = models.Categorie.objects.all()
    return render(request, "ludotheque/main.html", {"liste": liste})