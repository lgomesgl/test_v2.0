# Generated by Django 4.2 on 2023-05-24 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_enterprise_sponsorcompany_alter_email_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Person',
            new_name='People',
        ),
        migrations.AlterModelOptions(
            name='people',
            options={'verbose_name': 'People', 'verbose_name_plural': 'People'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Project', 'verbose_name_plural': 'Project'},
        ),
    ]