# Generated by Django 3.0.5 on 2020-05-01 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0005_bidders_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bidders',
            name='rating',
        ),
    ]
