# Generated by Django 4.2 on 2023-05-01 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_empresas_options_alter_pessoas_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projeto',
            old_name='nome',
            new_name='Nome do projeto',
        ),
    ]