# Generated by Django 2.1.2 on 2020-08-05 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0013_auto_20200805_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_detailes',
            name='Division',
            field=models.TextField(choices=[('1', 'Staffing'), ('2', 'Training'), ('3', 'IT Services')], default='Staffing', max_length=20),
        ),
    ]
