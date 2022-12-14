# Generated by Django 4.1.1 on 2022-10-03 12:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("post_reactions", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Dislike",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "owner_dislike",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="owner_dislike",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "post_dislike",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="post_dislike",
                        to="posts.post",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Like",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "owner_like",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="owner_like",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "post_like",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="post_like",
                        to="posts.post",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Vote",
        ),
    ]
