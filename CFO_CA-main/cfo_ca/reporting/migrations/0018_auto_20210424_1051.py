# Generated by Django 2.2 on 2021-04-24 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0017_scriptmaster'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scriptmaster',
            options={'ordering': ['script_id'], 'verbose_name': 'ScriptMaster', 'verbose_name_plural': 'ScriptMaster'},
        ),
    ]
