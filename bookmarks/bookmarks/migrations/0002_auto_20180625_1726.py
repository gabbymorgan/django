# Generated by Django 2.0.6 on 2018-06-25 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookmark',
            old_name='content',
            new_name='url',
        ),
    ]