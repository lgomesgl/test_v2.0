# Generated by Django 4.2 on 2023-05-24 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_idperson_reasearch_person_reasearch_project'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Project'},
        ),
    ]