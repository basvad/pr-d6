# Generated by Django 2.2.6 on 2020-06-28 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0006_book_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='p_library/static/photo'),
        ),
    ]