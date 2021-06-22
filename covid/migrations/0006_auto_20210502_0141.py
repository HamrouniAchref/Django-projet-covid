# Generated by Django 3.2 on 2021-05-02 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0005_auto_20210319_2320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maladie',
            name='vaccinateurs',
        ),
        migrations.AddField(
            model_name='vaccinateur',
            name='maladies',
            field=models.ManyToManyField(to='covid.Maladie'),
        ),
    ]
