# Generated by Django 3.1.7 on 2021-03-19 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0003_vaccinateur'),
    ]

    operations = [
        migrations.CreateModel(
            name='Declaration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('dateSymtomes', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EffetSecondaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('description', models.TextField()),
                ('members', models.ManyToManyField(through='covid.Declaration', to='covid.Vaccinateur')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='declaration',
            name='effetScondaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='covid.effetsecondaire'),
        ),
        migrations.AddField(
            model_name='declaration',
            name='vaccinateur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='covid.vaccinateur'),
        ),
    ]