# Generated by Django 4.1.1 on 2022-10-03 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="no_of_dislikes",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="post",
            name="no_of_likes",
            field=models.IntegerField(default=0),
        ),
    ]
