# Generated by Django 3.0.6 on 2020-05-20 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0013_auto_20200520_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback_mosquitokilling',
            name='service',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='feed.service'),
        ),
    ]
