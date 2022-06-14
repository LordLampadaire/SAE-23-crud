from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path("ajoutjeux/", views.ajoutjeux),
    path("traitementjeux/", views.traitementjeux),
    path('affiche/<int:id>/', views.affiche),
    path('update/<int:id>/', views.update),
    path('traitementupdate/<int:id>', views.traitementupdate),
    path('delete/<int:id>/', views.delete),
]