# Generated by Django 4.1.5 on 2023-02-25 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encyclopedia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='Completed',
            field=models.FloatField(null=True),
        ),
    ]