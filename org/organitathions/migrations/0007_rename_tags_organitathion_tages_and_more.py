# Generated by Django 5.0.3 on 2024-03-15 15:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organitathions', '0006_alter_organitathion_adress'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organitathion',
            old_name='tags',
            new_name='tages',
        ),
        migrations.AlterField(
            model_name='account',
            name='organitathion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='organitathions.organitathion'),
        ),
    ]
