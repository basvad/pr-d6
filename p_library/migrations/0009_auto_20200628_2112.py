# Generated by Django 2.2.6 on 2020-06-28 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0008_auto_20200628_2102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='avatar',
            new_name='photo',
        ),
    ]
