# Generated by Django 4.2 on 2023-06-12 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_over_date_project_over_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='people',
            old_name='Post',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='people',
            old_name='projeto',
            new_name='project',
        ),
        migrations.RenameField(
            model_name='people',
            old_name='Sex',
            new_name='sex',
        ),
    ]