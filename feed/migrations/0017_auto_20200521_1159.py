# Generated by Django 3.0.6 on 2020-05-21 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0016_auto_20200521_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completion_pondcleaning',
            name='automatic_skimmer',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='completion_pondcleaning',
            name='beneficial_bacteria',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
