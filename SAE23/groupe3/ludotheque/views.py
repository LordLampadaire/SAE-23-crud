from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import JeuxForm, JoueurForm, EditeurForm, CategorieForm, CommentaireForm
from . import models

# Create your views here.
def index(request):
    return render(request, 'ludotheque/main.html')


def ajoutjeux(request):
    if request.method == "POST":
        form = (request)
        if form.is_valid():
            jeu = form.save()
            return render(request, "ludotheque/affichejeu.html", {"jeu" : jeu})
        else:
            return render(request, "ludotheque/ajoutjeu.html", {"form" : form})
    else:
        form = JeuxForm()
        return render(request, "ludotheque/ajoutjeu.html", {"form" : form})


def traitementjeu(request):
    lform = JeuxForm(request.POST)
    if lform.is_valid():
        jeu = lform.save()
        return HttpResponseRedirect("/ludotheque/main")
    else:
        return render(request, "ludotheque/ajoutjeu.html", {"form" : lform})


def alljeu(request):
    liste = models.Jeux.objects.all()
    return render(request, "ludotheque/main.html", {"liste" : liste})


def affichejeu(request, id):
    jeu = models.Jeux.objects.get(pk=id)
    #liste = models.Disque.objects.all()
    return render(request, "ludotheque/affichejeu.html", {"jeu" : jeu})


def updatejeu(request, id):
    disquaire = models.Jeux.objects.get(pk=id)
    lform = JeuxForm(disquaire.dico())
    return render(request, "ludotheque/updatejeu.html", {"form": lform, "id" : id})


def traitementupdatejeu(request, id):
    lform = JeuxForm(request.POST)
    if lform.is_valid():
        jeu = lform.save(commit=False)
        jeu.id = id
        jeu.save()
        return HttpResponseRedirect("/ludotheque/main")
    else:
        return render(request, "ludotheque/updatejeu.html", {"form": lform, "id": id})


def deletejeu(request, id):
    jeu = models.Jeux.objects.get(pk=id)
    jeu.delete()
    return HttpResponseRedirect("/ludotheque/main")