# Generated by Django 3.0.3 on 2020-05-19 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0009_auto_20200512_1715'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='tags',
            new_name='categories',
        ),
    ]