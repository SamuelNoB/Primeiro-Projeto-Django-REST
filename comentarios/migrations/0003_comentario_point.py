# Generated by Django 3.0.5 on 2020-04-25 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200425_1637'),
        ('comentarios', '0002_auto_20200425_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='point',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='core.PontoTuristico', verbose_name='Ponto Turístico'),
            preserve_default=False,
        ),
    ]
