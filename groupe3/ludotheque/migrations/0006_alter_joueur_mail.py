# Generated by Django 4.0.5 on 2022-06-15 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ludotheque', '0005_jeux_editeur_alter_editeur_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joueur',
            name='mail',
            field=models.EmailField(help_text='A valid email address, please.', max_length=254),
        ),
    ]
