from django.db import models


class Editeur(models.Model):
    # idediteur = models.AutoField(db_column='idEditeur', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(max_length=45)
    date = models.IntegerField(blank=True, null=True)
    logo = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nom} a ete cree le {self.date}"

    def dico(self):
        return {"nom": self.nom, "date": self.date, "logo": self.logo}


class Categorie(models.Model):
    # idcategorie = models.AutoField(db_column='idCategorie', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(max_length=45)
    description = models.TextField()

    def __str__(self):
        return f"{self.nom} est defini par {self.description}"

    def dico(self):
        return {"nom": self.nom, "description": self.description}



class Jeux(models.Model):
    # idjeux = models.AutoField(db_column='idJeux', primary_key=True)  # Field name made lowercase.
    titre = models.CharField(max_length=45)
    date_sortie = models.CharField(max_length=45)
    photo = models.TextField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, db_column='Categorie_idCategorie', default=1)  # Field name made lowercase.

    def __str__(self):
        return f"{self.titre} est sorti le {self.date_sortie} fait partie de la categorie {self.categorie}"

    def dico(self):
        return {"titre": self.titre, "date_sortie": self.date_sortie, "photo": self.photo}


class Joueur(models.Model):
    # idjoueur = models.AutoField(db_column='idJoueur', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(max_length=45)
    prenom = models.CharField(max_length=45)
    mail = models.CharField(max_length=50)
    mdp = models.CharField(max_length=45)
    type = models.IntegerField()

    def __str__(self):
        return f"{self.nom} {self.prenom} a comme adresse mail {self.mail}"

    def dico(self):
        return {"nom": self.nom, "prenom": self.prenom, "mail": self.mail, "mdp": self.mdp, "type": self.type}

class Commentaire(models.Model):
    # idcommentaire = models.AutoField(db_column='idCommentaire', primary_key=True)  # Field name made lowercase.
    jeux = models.ForeignKey(Jeux, on_delete=models.CASCADE)
    joueur = models.ForeignKey(Joueur, on_delete=models.CASCADE)
    note = models.IntegerField()
    commentaire = models.TextField()
    date = models.DateField()
    #jeux_idjeux = models.ForeignKey('Jeux', models.DO_NOTHING, db_column='Jeux_idJeux')  # Field name made lowercase.

    def __str__(self):
        return f"Le {self.date}, {self.joueur} a commente {self.jeux} en expliquant que {self.commentaire}"

    def dico(self):
        return {"note": self.note, "commentaire": self.commentaire, "date": self.date}



class JeuxhasEditeur(models.Model):
    jeux = models.ForeignKey(Jeux, on_delete=models.CASCADE)
    editeur = models.ForeignKey(Editeur, on_delete=models.CASCADE)