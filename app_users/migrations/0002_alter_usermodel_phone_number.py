# Generated by Django 5.1.3 on 2024-11-06 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='phone_number',
            field=models.CharField(max_length=13),
        ),
    ]