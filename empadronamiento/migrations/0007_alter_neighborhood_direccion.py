# Generated by Django 3.2.1 on 2021-05-19 15:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('empadronamiento', '0006_alter_neighborhood_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighborhood',
            name='direccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
