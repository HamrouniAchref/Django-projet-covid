# Generated by Django 3.2 on 2021-05-08 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0009_vaccinateur_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaccinateur',
            name='email',
            field=models.EmailField(default='exemple@gmail.com', max_length=254, unique=True),
        ),
    ]