# Generated by Django 3.2.3 on 2021-06-08 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]