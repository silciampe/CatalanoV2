# Generated by Django 5.1.3 on 2025-02-18 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CatalanoBackend', '0006_alter_premio_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='premio',
            name='imagen',
            field=models.ImageField(upload_to='imagenes/premios'),
        ),
    ]
