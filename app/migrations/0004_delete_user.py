# Generated by Django 4.0.6 on 2022-07-14 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_offer_title'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]