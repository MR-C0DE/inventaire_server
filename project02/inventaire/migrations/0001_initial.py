# Generated by Django 4.1.2 on 2022-10-27 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('sorte', models.CharField(max_length=200)),
                ('quantite', models.IntegerField()),
                ('seuil', models.IntegerField()),
            ],
        ),
    ]