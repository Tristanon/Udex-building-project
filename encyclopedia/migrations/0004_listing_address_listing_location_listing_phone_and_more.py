# Generated by Django 4.1.5 on 2023-02-26 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encyclopedia', '0003_listing_architect_listing_materials_listing_namefor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='Address',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='Location',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='Phone',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='Completed',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='NameFor',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
