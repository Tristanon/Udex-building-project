# Generated by Django 4.1.5 on 2023-02-25 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encyclopedia', '0002_listing_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='Architect',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='Materials',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='NameFor',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='Style',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
