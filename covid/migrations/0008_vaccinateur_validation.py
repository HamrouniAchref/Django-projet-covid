# Generated by Django 3.2 on 2021-05-08 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0007_alter_vaccinateur_maladies'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaccinateur',
            name='validation',
            field=models.BooleanField(default=False),
        ),
    ]
