# Generated by Django 4.2.11 on 2024-07-11 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapingApp', '0003_websites_sitemap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websites',
            name='delivry_price',
            field=models.FloatField(),
        ),
    ]
