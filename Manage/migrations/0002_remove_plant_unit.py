# Generated by Django 5.0.3 on 2024-04-01 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plant',
            name='unit',
        ),
    ]
