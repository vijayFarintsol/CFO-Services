# Generated by Django 2.2 on 2021-04-08 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tally', '0013_merge_20210408_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='customgroup',
            name='closing_balance',
            field=models.DecimalField(blank=True, decimal_places=4, default=0.0, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='customgroup',
            name='opening_balance',
            field=models.DecimalField(blank=True, decimal_places=4, default=0.0, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='closing_balance',
            field=models.DecimalField(blank=True, decimal_places=4, default=0.0, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='opening_balance',
            field=models.DecimalField(blank=True, decimal_places=4, default=0.0, max_digits=20, null=True),
        ),
    ]
