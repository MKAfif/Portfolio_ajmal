# Generated by Django 4.2.5 on 2023-09-30 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolio',
            old_name='desciption',
            new_name='description',
        ),
    ]