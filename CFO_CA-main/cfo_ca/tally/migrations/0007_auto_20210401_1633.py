# Generated by Django 2.2 on 2021-04-01 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tally', '0006_auto_20210401_0620'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customgroup',
            name='group_type',
        ),
        migrations.RemoveField(
            model_name='group',
            name='group_type',
        ),
    ]
