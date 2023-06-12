# Generated by Django 4.2 on 2023-06-11 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_customuser_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='Over date',
            new_name='over_date',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='group',
            field=models.CharField(blank=True, choices=[('Admin', 'Admin'), ('SponsorCompony', 'SponsorCompony'), ('IC', 'IC')], max_length=50),
        ),
        migrations.AlterField(
            model_name='email',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='people',
            name='Post',
            field=models.CharField(choices=[('Professor Doutor', 'Professor Doutor'), ('Professor Adjunto', 'Professor Adjunto'), ('Pesquisador', 'Pesquisador'), ('Pós-Doc', 'Pós-Doc'), ('Doutorando', 'Doutorando'), ('Mestrando', 'Mestrando'), ('Iniciação científica', 'Iniciação científica')], max_length=50),
        ),
    ]
