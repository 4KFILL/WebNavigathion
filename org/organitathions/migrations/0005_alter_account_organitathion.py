# Generated by Django 5.0.3 on 2024-03-15 14:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organitathions', '0004_remove_comment_parent_comment_children'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='organitathion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='organitathions.organitathion'),
        ),
    ]
