# Generated by Django 4.2 on 2023-05-28 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_files_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='file',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='reasearchline',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='videos',
        ),
        migrations.RemoveField(
            model_name='videos',
            name='file',
        ),
    ]