# Generated by Django 3.0.5 on 2020-05-02 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0006_remove_bidders_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='feedback',
            field=models.TextField(default='No Feedback'),
        ),
    ]
