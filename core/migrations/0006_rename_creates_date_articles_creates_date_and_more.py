# Generated by Django 4.2 on 2023-06-16 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_post_people_position'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='Creates date',
            new_name='Creates_date',
        ),
        migrations.RenameField(
            model_name='articles',
            old_name='Modify date',
            new_name='Modify_date',
        ),
        migrations.RenameField(
            model_name='email',
            old_name='Creates date',
            new_name='Creates_date',
        ),
        migrations.RenameField(
            model_name='email',
            old_name='Modify date',
            new_name='Modify_date',
        ),
        migrations.RenameField(
            model_name='files',
            old_name='Creates date',
            new_name='Creates_date',
        ),
        migrations.RenameField(
            model_name='files',
            old_name='Modify date',
            new_name='Modify_date',
        ),
        migrations.RenameField(
            model_name='metadata',
            old_name='Creates date',
            new_name='Creates_date',
        ),
        migrations.RenameField(
            model_name='metadata',
            old_name='Modify date',
            new_name='Modify_date',
        ),
        migrations.RenameField(
            model_name='people',
            old_name='Creates date',
            new_name='Creates_date',
        ),
        migrations.RenameField(
            model_name='people',
            old_name='Modify date',
            new_name='Modify_date',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='Creates date',
            new_name='Creates_date',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='Modify date',
            new_name='Modify_date',
        ),
        migrations.RenameField(
            model_name='reasearchlines',
            old_name='Creates date',
            new_name='Creates_date',
        ),
        migrations.RenameField(
            model_name='reasearchlines',
            old_name='Modify date',
            new_name='Modify_date',
        ),
        migrations.RenameField(
            model_name='sponsorcompany',
            old_name='Creates date',
            new_name='Creates_date',
        ),
        migrations.RenameField(
            model_name='sponsorcompany',
            old_name='Modify date',
            new_name='Modify_date',
        ),
        migrations.RenameField(
            model_name='videos',
            old_name='Creates date',
            new_name='Creates_date',
        ),
        migrations.RenameField(
            model_name='videos',
            old_name='Modify date',
            new_name='Modify_date',
        ),
        migrations.AlterField(
            model_name='people',
            name='position',
            field=models.CharField(choices=[('Professors', 'Professors'), ('Collaborating Professors', 'Collaborating Professors'), ('Researchers', 'Researchers'), ('Postdocs', 'Postdocs'), ('Ph.D students', 'Ph.D students'), ('Master Students', 'Master Students'), ('Graduation Students', 'Graduation Students'), ('Tech staff', 'Tech staff'), ('Project Manager', 'Project Manager')], max_length=50),
        ),
    ]
