# Generated by Django 2.1 on 2019-07-29 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teste', '0011_favorite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favorite',
            old_name='movie_id',
            new_name='movie',
        ),
        migrations.RenameField(
            model_name='favorite',
            old_name='user_id',
            new_name='user',
        ),
    ]
