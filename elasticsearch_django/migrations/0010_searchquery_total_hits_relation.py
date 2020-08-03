# Generated by Django 3.0.8 on 2020-07-29 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("elasticsearch_django", "0009_searchquery_query_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="searchquery",
            name="total_hits_relation",
            field=models.CharField(
                blank=True,
                choices=[
                    ("eq", "Accurate hit count"),
                    ("gte", "Lower bound of total hits"),
                ],
                default="",
                help_text="Indicates whether this is an exact match ('eq') or a lower bound ('gte')",
                max_length=3,
            ),
        ),
    ]
