# Generated by Django 4.2 on 2023-05-01 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_alter_projeto_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projeto',
            options={},
        ),
        migrations.RenameField(
            model_name='projeto',
            old_name='Nome do projeto',
            new_name='nome',
        ),
    ]