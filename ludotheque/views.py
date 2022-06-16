from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import JeuxForm, JoueurForm, EditeurForm, CategorieForm, CommentaireForm
from . import models

def index(request):
    return render(request, 'ludotheque/main.html')

def ajoutjeux(request):
    if request.method == "POST":
        form = (request)
        if form.is_valid():
            jeux = form.save()
            return HttpResponseRedirect("/ludotheque/")
        else:
            return render(request, "ludotheque/ajoutjeux.html", {"form": form})
    else:
        form = JeuxForm()
        return render(request, "ludotheque/ajoutjeux.html", {"form" : form})


def traitementjeux(request):
    jform = JeuxForm(request.POST)
    if jform.is_valid():
        jeux = jform.save()
        return HttpResponseRedirect("/ludotheque/")
    else:
        return render(request,"ludotheque/ajoutjeux.html",{"form": jform})


def index(request):
    liste = list(models.Jeux.objects.all())
    return render(request, 'ludotheque/index.html', {'liste': liste})

def affiche(request, id):
    jeux = models.Jeux.objects.get(pk=id)
    return render(request,"ludotheque/affiche.html",{"Jeux" : jeux})

def delete(request, id):
    jeux = models.Jeux.objects.get(pk=id)
    jeux.delete()
    return HttpResponseRedirect("/ludotheque/")

def update(request, id):
    Jeux = models.Jeux.objects.get(pk=id)
    jform = JeuxForm(Jeux.dico())
    return render(request, "ludotheque/update.html", {"form": jform,"id":id})


def traitementupdate(request, id):
    jform = JeuxForm(request.POST)
    if jform.is_valid():
        jeux = jform.save(commit=False)
        jeux.id = id;
        jeux.save()
        return HttpResponseRedirect("/ludotheque/")
    else:
        return render(request, "ludotheque/update.html", {"form": jform, "id": id})

def ok(request):
    return render(request, 'index.html')