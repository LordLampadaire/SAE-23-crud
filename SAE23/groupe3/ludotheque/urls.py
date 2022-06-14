from django.urls import path
from . import views



urlpatterns = [
    path('main/', views.index),
    path("ajoutjeu/", views.ajoutjeux),
    path("traitementjeu", views.traitementjeu),
    path('affichejeu/<int:id>/', views.affichejeu),
    path('updatejeu/<int:id>/', views.updatejeu),
    path('traitementupdatejeu/<int:id>', views.traitementupdatejeu),
    path('deletejeu/<int:id>/', views.deletejeu),
]
