# Generated by Django 2.1.2 on 2020-08-05 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0014_auto_20200805_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_detailes',
            name='Division',
            field=models.TextField(choices=[('1', 'Staffing'), ('2', 'Training'), ('3', 'IT Services')], default='1', max_length=20),
        ),
        migrations.AlterField(
            model_name='company_detailes',
            name='Sector',
            field=models.TextField(choices=[('1', 'USA'), ('2', 'India')], default='2', max_length=20),
        ),
    ]
