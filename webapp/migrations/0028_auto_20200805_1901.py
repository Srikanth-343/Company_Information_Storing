# Generated by Django 2.1.2 on 2020-08-05 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0027_auto_20200805_1850'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company_detailes',
            old_name='NUMBER_employees',
            new_name='Number',
        ),
        migrations.AlterField(
            model_name='company_detailes',
            name='Number_of_Internal_Employees',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
