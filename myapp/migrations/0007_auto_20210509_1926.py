# Generated by Django 3.1.5 on 2021-05-09 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20210509_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='nowtime',
            field=models.CharField(max_length=50),
        ),
    ]
