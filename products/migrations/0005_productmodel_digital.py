# Generated by Django 3.1.5 on 2021-01-19 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20201214_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='digital',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
