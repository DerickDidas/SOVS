# Generated by Django 4.0.6 on 2022-08-08 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollapp', '0003_rename_tee_candidate_nida_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='image',
            field=models.ImageField(default=1, upload_to='pics'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='candidate',
            name='NIDA_NUMBER',
            field=models.IntegerField(),
        ),
    ]