# Generated by Django 2.1.2 on 2020-08-06 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0030_auto_20200805_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='company_detailes',
            name='Website',
            field=models.TextField(help_text='www.abc.com', null=True),
        ),
    ]
