# Generated by Django 3.2 on 2021-05-18 04:23

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0016_bookmovie_seat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviepost',
            name='trailer',
            field=embed_video.fields.EmbedVideoField(),
        ),
    ]
