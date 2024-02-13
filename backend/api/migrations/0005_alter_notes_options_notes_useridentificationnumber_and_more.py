# Generated by Django 5.0.2 on 2024-02-13 17:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_alter_user_username"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="notes",
            options={"ordering": ["-updatedAt"]},
        ),
        migrations.AddField(
            model_name="notes",
            name="userIdentificationNumber",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="api.user"
            ),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=20)),
                (
                    "userIdentificationNumber",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.user"
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="notes",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="api.category"
            ),
        ),
    ]