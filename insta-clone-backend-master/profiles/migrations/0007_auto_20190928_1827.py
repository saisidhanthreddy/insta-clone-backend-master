# Generated by Django 2.2.5 on 2019-09-28 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_connections'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]