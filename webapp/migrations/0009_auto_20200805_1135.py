# Generated by Django 2.1.2 on 2020-08-05 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_auto_20200805_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_detailes',
            name='Company',
            field=models.TextField(max_length=80),
        ),
    ]