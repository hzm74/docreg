# Generated by Django 3.1.5 on 2021-03-12 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_auto_20210311_1434'),
    ]

    operations = [
        migrations.CreateModel(
            name='Controlemomenten_gepland',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ter_eerste_controle_gepland', models.DateField()),
                ('ter_eerste_controle_retour_binnen_gepland', models.DateField()),
                ('ter_tweede_controle_gepland', models.DateField()),
                ('ter_tweede_controle_retour_binnen_gepland', models.DateField()),
                ('definitief_binnen_gepland', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Geplande controlemomenten',
            },
        ),
        migrations.RenameField(
            model_name='vloeren',
            old_name='definitief_binnen_gepland',
            new_name='datum_document',
        ),
        migrations.RemoveField(
            model_name='vloeren',
            name='ter_eerste_controle_gepland',
        ),
        migrations.RemoveField(
            model_name='vloeren',
            name='ter_eerste_controle_retour_binnen_gepland',
        ),
        migrations.RemoveField(
            model_name='vloeren',
            name='ter_tweede_controle_gepland',
        ),
        migrations.RemoveField(
            model_name='vloeren',
            name='ter_tweede_controle_retour_binnen_gepland',
        ),
    ]
