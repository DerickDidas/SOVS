# Generated by Django 4.0.6 on 2022-08-07 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pollapp', '0002_candidate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='tee',
            new_name='NIDA_NUMBER',
        ),
        migrations.RenameField(
            model_name='candidate',
            old_name='img',
            new_name='image',
        ),
    ]