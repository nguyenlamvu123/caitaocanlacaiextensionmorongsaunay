# Generated by Django 2.2 on 2020-01-09 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idol', '0002_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idol',
            name='birthday',
            field=models.DateTimeField(blank=True),
        ),
    ]
