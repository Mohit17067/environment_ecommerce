# Generated by Django 3.0.6 on 2020-05-20 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0014_auto_20200520_2219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback_mosquitokilling',
            name='repallant_name',
        ),
        migrations.AlterField(
            model_name='feedback_mosquitokilling',
            name='natural_repallant',
            field=models.CharField(blank=True, default='None', max_length=200, null=True),
        ),
    ]