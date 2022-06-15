# Generated by Django 4.0.5 on 2022-06-15 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=45)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Editeur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=45)),
                ('date', models.IntegerField(blank=True, null=True)),
                ('logo', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Jeux',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=45)),
                ('date_sortie', models.CharField(max_length=45)),
                ('photo', models.URLField(blank=True)),
                ('categorie', models.ForeignKey(db_column='Categorie_idCategorie', default=1, on_delete=django.db.models.deletion.CASCADE, to='ludotheque.categorie')),
            ],
        ),
        migrations.CreateModel(
            name='Joueur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=45)),
                ('prenom', models.CharField(max_length=45)),
                ('mail', models.CharField(max_length=50)),
                ('mdp', models.CharField(max_length=45)),
                ('type', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='JeuxhasEditeur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('editeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ludotheque.editeur')),
                ('jeu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ludotheque.jeux')),
            ],
        ),
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.IntegerField()),
                ('commentaire', models.TextField()),
                ('date', models.DateField()),
                ('jeu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ludotheque.jeux')),
                ('joueur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ludotheque.joueur')),
            ],
        ),
    ]
