from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import JeuxForm, JoueurForm, EditeurForm, CategorieForm, CommentaireForm
from . import models
import operator



# Create your views here.

def index(request):
    catego = list(models.Categorie.objects.all())
    jeu = list(models.Jeux.objects.all())
    joueur = list(models.Joueur.objects.all())
    editeur = list(models.Editeur.objects.all())
    commentaire = list(models.Commentaire.objects.all())
    return render(request, 'ludotheque/main.html', {"catego": catego, "jeu": jeu, "joueur": joueur, 'editeur': editeur, 'commentaire': commentaire})



## editeur

def indexediteur(request):
    catego = list(models.Categorie.objects.all())
    jeu = list(models.Jeux.objects.all())
    joueur = list(models.Joueur.objects.all())
    editeur = list(models.Editeur.objects.all())
    commentaire = list(models.Commentaire.objects.all())
    return render(request, 'ludotheque/editeur/mainediteur.html', {"catego": catego, "jeu": jeu, "joueur": joueur, 'editeur': editeur, 'commentaire': commentaire})



def ajoutediteur(request):
    if request.method == "POST":
        form = (request)
        if form.is_valid():
            editeur = form.save()
            return render(request, "ludotheque/editeur/afficheediteur.html", {"editeur" : editeur})
        else:
            return render(request, "ludotheque/editeur/ajoutediteur.html", {"form" : form})
    else:
        form = EditeurForm()
        return render(request, "ludotheque/editeur/ajoutediteur.html", {"form" : form})


def traitementediteur(request):
    lform = EditeurForm(request.POST)
    if lform.is_valid():
        editeur = lform.save()
        return HttpResponseRedirect("/ludotheque/editeur/mainediteur")
    else:
        return render(request, "ludotheque/editeur/ajoutediteur.html", {"form" : lform})


"""def allediteur(request):
    liste = models.Editeur.objects.all()
    return render(request, "ludotheque/main.html", {"liste" : liste})"""


def afficheediteur(request, id):
    editeur = models.Editeur.objects.get(pk=id)
    return render(request, "ludotheque/editeur/afficheediteur.html", {"editeur" : editeur})


def updateediteur(request, id):
    editeur = models.Editeur.objects.get(pk=id)
    lform = EditeurForm(editeur.dico())
    return render(request, "ludotheque/editeur/updateediteur.html", {"form": lform, "id" : id})


def traitementupdateediteur(request, id):
    lform = EditeurForm(request.POST)
    if lform.is_valid():
        editeur = lform.save(commit=False)
        editeur.id = id
        editeur.save()
        return HttpResponseRedirect("/ludotheque/editeur/mainediteur")
    else:
        return render(request, "ludotheque/editeur/updateediteur.html", {"form": lform, "id": id})


def deleteediteur(request, id):
    editeur = models.Editeur.objects.get(pk=id)
    editeur.delete()
    return HttpResponseRedirect("/ludotheque/main")



#jeu

def indexjeu(request):
    catego = list(models.Categorie.objects.all())
    jeu = list(models.Jeux.objects.all())
    joueur = list(models.Joueur.objects.all())
    editeur = list(models.Editeur.objects.all())
    commentaire = list(models.Commentaire.objects.all())
    return render(request, 'ludotheque/jeu/mainjeu.html', {"catego": catego, "jeu": jeu, "joueur": joueur, 'editeur': editeur, 'commentaire': commentaire})


def ajoutjeux(request):
    if request.method == "POST":
        form = (request)
        if form.is_valid():
            jeu = form.save()
            return render(request, "ludotheque/jeu/affichejeu.html", {"jeu" : jeu})
        else:
            return render(request, "ludotheque/jeu/ajoutjeu.html", {"form" : form})
    else:
        form = JeuxForm()
        return render(request, "ludotheque/jeu/ajoutjeu.html", {"form" : form})


def traitementjeu(request):
    lform = JeuxForm(request.POST)
    if lform.is_valid():
        jeu = lform.save()
        return HttpResponseRedirect("/ludotheque/jeu/mainjeu")
    else:
        return render(request, "ludotheque/jeu/ajoutjeu.html", {"form" : lform})



def affichejeu(request, id):
    jeu = models.Jeux.objects.get(pk=id)
    commentaire = models.Commentaire.objects.all()
    #list_com = list(models.Commentaire.objects.all())
    liste1, compt1 = 0, 0
    liste2, compt2 = 0, 0
    note_max, note_min = 0, 10
    com1, com2 = None, None
    taille =0


    for c in commentaire:
        if c.jeu == jeu:
            taille +=1
            if c.note >= note_max:
                com1 = c
                note_max = c.note
            if c.note <= note_min:
                com2 = c
                note_min = c.note


    for c in commentaire:
        a = c.joueur
        if c.jeu == jeu:
            if a.type == 'Professionnel':
                liste1 += c.note
                compt1 += 1
            else:
                liste2 += c.note
                compt2 += 1
    if compt1 == 0:
        moyenne1 = 0
    else:
        moyenne1 = round((liste1 / compt1), 1)
    if compt2 == 0:
        moyenne2 = 0
    else:
        moyenne2 = round((liste2 / compt2), 1)
    return render(request, "ludotheque/jeu/affichejeu.html",
                      {"jeu": jeu, "commentaire": commentaire, "pro" : moyenne1, "part": moyenne2, "com1": com1, "com2": com2, "taille": taille})


def updatejeu(request, id):
    jeu = models.Jeux.objects.get(pk=id)
    lform = JeuxForm(jeu.dico())
    return render(request, "ludotheque/jeu/updatejeu.html", {"form": lform, "id" : id})


def traitementupdatejeu(request, id):
    lform = JeuxForm(request.POST)
    if lform.is_valid():
        jeu = lform.save(commit=False)
        jeu.id = id
        jeu.save()
        return HttpResponseRedirect("/ludotheque/jeu/mainjeu")
    else:
        return render(request, "ludotheque/jeu/updatejeu.html", {"form": lform, "id": id})


def deletejeu(request, id):
    jeu = models.Jeux.objects.get(pk=id)
    jeu.delete()
    return HttpResponseRedirect("/ludotheque/main")









##categories


def ajoutcategorie(request):
    if request.method == "POST":
        form = (request)
        if form.is_valid():
            catego = form.save()
            return render(request, "ludotheque/categorie/affichecatego.html", {"catego" : catego})
        else:
            return render(request, "ludotheque/categorie/ajoutcatego.html", {"form" : form})
    else:
        form = CategorieForm()
        return render(request, "ludotheque/categorie/ajoutcatego.html", {"form" : form})


def traitementcategorie(request):
    lform = CategorieForm(request.POST)
    if lform.is_valid():
        catego = lform.save()
        return HttpResponseRedirect("/ludotheque/main")
    else:
        return render(request, "ludotheque/categorie/ajoutcatego.html", {"form" : lform})


def affichecategorie(request, id):
    categorie = models.Categorie.objects.get(pk=id)
    jeu = models.Jeux.objects.all()
    return render(request, "ludotheque/categorie/affichecatego.html", {"categorie" : categorie, 'jeu': jeu})


def updatecategorie(request, id):
    catego = models.Categorie.objects.get(pk=id)
    lform = CategorieForm(catego.dico())
    return render(request, "ludotheque/categorie/updatecatego.html", {"form": lform, "id" : id})


def traitementupdatecategorie(request, id):
    lform = CategorieForm(request.POST)
    if lform.is_valid():
        catego = lform.save(commit=False)
        catego.id = id
        catego.save()
        return HttpResponseRedirect("/ludotheque/main")
    else:
        return render(request, "ludotheque/categorie/updatecatego.html", {"form": lform, "id": id})


def deletecategorie(request, id):
    catego = models.Categorie.objects.get(pk=id)
    catego.delete()
    return HttpResponseRedirect("/ludotheque/main")



#joueur

def indexjoueur(request):
    catego = list(models.Categorie.objects.all())
    jeu = list(models.Jeux.objects.all())
    joueur = list(models.Joueur.objects.all())
    editeur = list(models.Editeur.objects.all())
    commentaire = list(models.Commentaire.objects.all())
    return render(request, 'ludotheque/joueur/mainjoueur.html', {"catego": catego, "jeu": jeu, "joueur": joueur, 'editeur': editeur, 'commentaire': commentaire})


def ajoutjoueur(request):
    if request.method == "POST":
        form = (request)
        if form.is_valid():
            joueur = form.save()
            return render(request, "ludotheque/joueur/affichejoueur.html", {"joueur" : joueur})
        else:
            return render(request, "ludotheque/joueur/ajoutjoueur.html", {"form" : form})
    else:
        form = JoueurForm()
        return render(request, "ludotheque/joueur/ajoutjoueur.html", {"form" : form})


def traitementjoueur(request):
    lform = JoueurForm(request.POST)
    if lform.is_valid():
        joueur = lform.save()
        return HttpResponseRedirect("/ludotheque/joueur/mainjoueur")
    else:
        return render(request, "ludotheque/joueur/ajoutjoueur.html", {"form" : lform})


def affichejoueur(request, id):
    joueur = models.Joueur.objects.get(pk=id)
    commentaire = models.Commentaire.objects.all()
    jeu = models.Jeux.objects.all()
    liste=[k for k in jeu]
    for c in commentaire:
        if c.joueur == joueur:
            if c.jeu in liste:
                liste.remove(c.jeu)

    return render(request, "ludotheque/joueur/affichejoueur.html", {"joueur" : joueur, "commentaire": commentaire, "liste": liste})


def updatejoueur(request, id):
    joueur = models.Joueur.objects.get(pk=id)
    lform = JoueurForm(joueur.dico())
    return render(request, "ludotheque/joueur/updatejoueur.html", {"form": lform, "id" : id})


def traitementupdatejoueur(request, id):
    lform = JoueurForm(request.POST)
    if lform.is_valid():
        joueur = lform.save(commit=False)
        joueur.id = id
        joueur.save()
        return HttpResponseRedirect("/ludotheque/joueur/mainjoueur")
    else:
        return render(request, "ludotheque/joueur/updatejoueur.html", {"form": lform, "id": id})


def deletejoueur(request, id):
    joueur = models.Joueur.objects.get(pk=id)
    joueur.delete()
    return HttpResponseRedirect("/ludotheque/main")




#commentaire

def ajoutcom(request):
    if request.method == "POST":
        form = (request)
        if form.is_valid():
            commentaire = form.save()
            return render(request, "ludotheque/commentaire/affichecommentaire.html", {"commentaire" : commentaire})
        else:
            return render(request, "ludotheque/commentaire/ajoutcommentaire.html", {"form" : form})
    else:
        form = CommentaireForm()
        return render(request, "ludotheque/commentaire/ajoutcommentaire.html", {"form" : form})


def traitementcom(request):
    lform = CommentaireForm(request.POST)
    if lform.is_valid():
        commentaire = lform.save()
        return HttpResponseRedirect("/ludotheque/main")
    else:
        return render(request, "ludotheque/commentaire/ajoutcommentaire.html", {"form" : lform})



def affichecommentaire(request, id):
    commentaire = models.Commentaire.objects.get(pk=id)
    return render(request, "ludotheque/commentaire/affichecommentaire.html", {"commentaire" : commentaire})


def updatecommentaire(request, id):
    commentaire = models.Commentaire.objects.get(pk=id)
    lform = CommentaireForm(commentaire.dico())
    return render(request, "ludotheque/commentaire/updatecommentaire.html", {"form": lform, "id" : id})


def traitementupdatecommentaire(request, id):
    lform = CommentaireForm(request.POST)
    if lform.is_valid():
        commentaire = lform.save(commit=False)
        commentaire.id = id
        commentaire.save()
        return HttpResponseRedirect("/ludotheque/main")
    else:
        return render(request, "ludotheque/commentaire/updatecommentaire.html", {"form": lform, "id": id})


def deletecommentaire(request, id):
    commentaire = models.Commentaire.objects.get(pk=id)
    commentaire.delete()
    return HttpResponseRedirect("/ludotheque/main")




## BROUILLON
#affichage meilleur et pire commentaire
"""d = dict()
    for c in commentaire:
        taille+=1
        k = c.id
        d[k] = c.note, c.jeu, c.joueur, c.commentaire
    df = list(sorted(d.items(), key=operator.itemgetter(0)))
    if taille >= 1:
        com1 = df[0]
        if taille >1:
            com2 = df[-1]"""