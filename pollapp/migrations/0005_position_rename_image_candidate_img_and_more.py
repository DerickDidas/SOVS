# Generated by Django 4.0.6 on 2022-08-13 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollapp', '0004_choice_image_alter_candidate_nida_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='candidate',
            old_name='image',
            new_name='img',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='NIDA_NUMBER',
        ),
        migrations.AlterField(
            model_name='candidate',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]