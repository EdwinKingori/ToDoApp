# Generated by Django 4.2.4 on 2024-03-09 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='User',
            new_name='user',
        ),
    ]
