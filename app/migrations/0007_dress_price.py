# Generated by Django 4.1.5 on 2023-02-02 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_dress_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='dress',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]
