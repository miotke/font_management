# Generated by Django 3.1.4 on 2020-12-18 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fonts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='font',
            name='checked_out',
            field=models.BooleanField(default=False),
        ),
    ]
