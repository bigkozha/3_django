# Generated by Django 3.0.7 on 2020-07-12 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_guess_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guess',
            old_name='owner',
            new_name='user',
        ),
    ]
