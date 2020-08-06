# Generated by Django 2.1.2 on 2020-08-05 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_auto_20200805_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_detailes',
            name='Division',
            field=models.TextField(choices=[('staffing', 'Staffing'), ('training', 'Training'), ('iT Services', 'IT Services')], default='Staffing', max_length=20),
        ),
        migrations.AlterField(
            model_name='company_detailes',
            name='Sector',
            field=models.TextField(choices=[('usa', 'USA'), ('india', 'India')], default='India', max_length=20),
        ),
    ]
