# Generated by Django 3.0.5 on 2020-05-24 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_pontoturistico_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pontoturistico',
            old_name='adress',
            new_name='address',
        ),
    ]
