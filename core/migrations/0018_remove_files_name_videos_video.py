# Generated by Django 4.2 on 2023-05-28 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_files_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='files',
            name='name',
        ),
        migrations.AddField(
            model_name='videos',
            name='video',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
