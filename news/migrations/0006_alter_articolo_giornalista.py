# Generated by Django 5.1.3 on 2025-02-12 08:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_articolo_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articolo',
            name='giornalista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articolo', to='news.giornalista'),
        ),
    ]
