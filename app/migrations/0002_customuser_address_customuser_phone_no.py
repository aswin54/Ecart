# Generated by Django 4.1.5 on 2023-01-30 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone_no',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
