# Generated by Django 3.2.1 on 2021-05-17 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empadronamiento', '0002_auto_20210517_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='departamento',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='piso',
            field=models.CharField(max_length=4, null=True),
        ),
    ]