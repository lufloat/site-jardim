# Generated by Django 5.2 on 2025-04-30 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0003_jardins_data_jardins'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jardins',
            name='foto',
            field=models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d/'),
        ),
    ]
