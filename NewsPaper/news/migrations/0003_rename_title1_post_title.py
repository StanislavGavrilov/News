# Generated by Django 4.2 on 2023-05-09 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_rename_title_post_title1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='title1',
            new_name='title',
        ),
    ]
