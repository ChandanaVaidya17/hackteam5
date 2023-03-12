# Generated by Django 4.1.4 on 2023-03-11 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="City",
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
                ("name", models.CharField(max_length=255)),
                ("image", models.ImageField(upload_to="city_images")),
                ("about", models.TextField(max_length=1000)),
                ("rating", models.CharField(max_length=2)),
                ("comments", models.CharField(max_length=1000)),
            ],
        ),
    ]
