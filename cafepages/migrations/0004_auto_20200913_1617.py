# Generated by Django 3.1 on 2020-09-13 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafepages', '0003_auto_20200913_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='fname',
            field=models.CharField(blank=True, default=None, max_length=10),
            preserve_default=False,
        ),
    ]
