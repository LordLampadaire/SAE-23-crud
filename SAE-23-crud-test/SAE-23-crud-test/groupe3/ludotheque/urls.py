from django.urls import path
from . import views



urlpatterns = [
    path('main/', views.index),
    path('mainjeu/', views.indexjeu),

    path("ajoutjeu/", views.ajoutjeux),
    path("traitementjeu", views.traitementjeu),
    path('affichejeu/<int:id>/', views.affichejeu),
    path('updatejeu/<int:id>/', views.updatejeu),
    path('traitementupdatejeu/<int:id>', views.traitementupdatejeu),
    path('deletejeu/<int:id>/', views.deletejeu),

    path("ajoutcatego/", views.ajoutcategorie),
    path("traitementcatego", views.traitementcategorie),
    path('affichecatego/<int:id>/', views.affichecategorie),
    path('updatecatego/<int:id>/', views.updatecategorie),
    path('traitementupdatecatego/<int:id>', views.traitementupdatecategorie),
    path('deletecatego/<int:id>/', views.deletecategorie),

    path("ajoutjoueur/", views.ajoutjoueur),
    path("traitementjoueur", views.traitementjoueur),
    path('affichejoueur/<int:id>/', views.affichejoueur),
    path('updatejoueur/<int:id>/', views.updatejoueur),
    path('traitementupdatejoueur/<int:id>', views.traitementupdatejoueur),
    path('deletejoueur/<int:id>/', views.deletejoueur),


    path("ajoutediteur/", views.ajoutediteur),
    path("traitementediteur", views.traitementediteur),
    path('afficheediteur/<int:id>/', views.afficheediteur),
    path('updateediteur/<int:id>/', views.updateediteur),
    path('traitementupdateediteur/<int:id>', views.traitementupdateediteur),
    path('deleteediteur/<int:id>/', views.deleteediteur),

    path("ajoutcommentaire/", views.ajoutcom),
    path("traitementcommentaire", views.traitementcom),
    path('affichecommentaire/<int:id>/', views.affichecommentaire),
    path('updatecommentaire/<int:id>/', views.updatecommentaire),
    path('traitementupdatecommentaire/<int:id>', views.traitementupdatecommentaire),
    path('deletecommentaire/<int:id>/', views.deletecommentaire),
]
