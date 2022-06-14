# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

# -*- coding: utf-8 -*-
from django.db import models


class Editeur(models.Model):
    idediteur = models.AutoField(db_column='idEditeur', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(max_length=45, blank=True, null=True)
    date = models.IntegerField(blank=True, null=True)
    logo = models.TextField(blank=True, null=True)
    #jeux = models.ForeignKey('titre', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'editeur'

    def __str__(self):
        return f"{self.nom} a ete cree le {self.date}"



class Categorie(models.Model):
    idcategorie = models.AutoField(db_column='idCategorie', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(max_length=45, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categorie'

    def __str__(self):
        return f"{self.nom} est defini par {self.description}"


class Commentaire(models.Model):
    idcommentaire = models.AutoField(db_column='idCommentaire', primary_key=True)  # Field name made lowercase.
    jeux = models.CharField(max_length=45, blank=True, null=True)
    joueur = models.CharField(max_length=45, blank=True, null=True)
    note = models.IntegerField(blank=True, null=True)
    commentaire = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    jeux_idjeux = models.ForeignKey('Jeux', models.DO_NOTHING, db_column='Jeux_idJeux')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'commentaire'
        unique_together = (('idcommentaire', 'jeux_idjeux'),)

    def __str__(self):
        return f"Le {self.date}, {self.joueur} a commente {self.jeux} en expliquant que {self.commentaire}"



class Jeux(models.Model):
    idjeux = models.AutoField(db_column='idJeux', primary_key=True)  # Field name made lowercase.
    titre = models.CharField(max_length=45, blank=True, null=True)
    date_sortie = models.CharField(max_length=45, blank=True, null=True)
    photo = models.TextField()
    categorie_idcategorie = models.ForeignKey(Categorie, models.DO_NOTHING, db_column='Categorie_idCategorie')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'jeux'
        unique_together = (('idjeux', 'categorie_idcategorie'),)

    def __str__(self):
        return f"{self.titre} est sorti le {self.date_sortie} fait partie de la categorie {self.categorie_idcategorie}"




class Joueur(models.Model):
    idjoueur = models.AutoField(db_column='idJoueur', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(max_length=45, blank=True, null=True)
    prenom = models.CharField(max_length=45, blank=True, null=True)
    mail = models.CharField(max_length=50, blank=True, null=True)
    mdp = models.CharField(max_length=45, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'joueur'

    def __str__(self):
        return f"{self.nom} {self.prenom} a comme adresse mail {self.mail}"


class JeuxhasEditeur(models.Model):
    jeux = models.ForeignKey(Jeux, on_delete=models.CASCADE, default='1')
    editeur = models.ForeignKey(Editeur, on_delete=models.CASCADE, default='1')



"""class JoueurHasJeux(models.Model):
    joueur_idjoueur = models.OneToOneField(Joueur, models.DO_NOTHING, db_column='Joueur_idJoueur', primary_key=True)  # Field name made lowercase.
    jeux_idjeux = models.ForeignKey(Jeux, models.DO_NOTHING, db_column='Jeux_idJeux')  # Field name made lowercase.
    jeux_categorie_idcategorie = models.ForeignKey(Jeux, models.DO_NOTHING, db_column='Jeux_Categorie_idCategorie')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'joueur_has_jeux'
        unique_together = (('joueur_idjoueur', 'jeux_idjeux', 'jeux_categorie_idcategorie'),)
"""

"""
class JeuxhasEditeur(models.Model):
    jeux_id = models.ManyToManyField(Jeux, models.DO_NOTHING, db_column='JeuxhasEditeur_idJeux')
    editeur_id = models.ForeignKey(Editeur, models.DO_NOTHING, db_column='JeuxhasEditeur_idEditeur')
    #auteur = models.ManyToManyField(auteur, through=Jeux_auteur)
    

    def __str__(self):
        return f"{self.jeux_id} a comme editeur {self.editeur_id}"
"""