# Generated by Django 3.1.5 on 2021-03-11 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bedrijven',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bedrijfsnaam', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Controlemomenten_gepland',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ter_eerste_controle_gepland', models.DateTimeField()),
                ('ter_eerste_controle_retour_binnen_gepland', models.DateTimeField()),
                ('ter_tweede_controle_gepland', models.DateTimeField()),
                ('ter_tweede_controle_retour_binnen_gepland', models.DateTimeField()),
                ('definitief_binnen_gepland', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Vloeren',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nummer', models.CharField(max_length=10)),
                ('documentnaam', models.CharField(max_length=50)),
            ],
        ),
    ]
