# Generated by Django 4.2 on 2023-05-28 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_files_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='type',
            field=models.CharField(blank=True, choices=[('PDF', 'PDF'), ('EXCEL', 'EXCEL'), ('WORD', 'WORD')], max_length=50),
        ),
    ]