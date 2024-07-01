# Generated by Django 5.0.3 on 2024-03-13 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organitathions', '0002_remove_comment_to_comment_comment_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='parent',
        ),
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ManyToManyField(blank=True, null=True, to='organitathions.comment', verbose_name='Родитель'),
        ),
    ]
