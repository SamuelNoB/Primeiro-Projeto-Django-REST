# Generated by Django 3.0.5 on 2020-05-20 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_pontoturistico_adress'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='pontos_turisticos'),
        ),
    ]
