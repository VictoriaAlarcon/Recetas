# Generated by Django 3.0.6 on 2020-08-02 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='website',
        ),
    ]
