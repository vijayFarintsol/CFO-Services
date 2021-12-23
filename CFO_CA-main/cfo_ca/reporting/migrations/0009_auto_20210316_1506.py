# Generated by Django 2.2 on 2021-03-16 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0008_celeryscheduletask_class_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='misreportscheduleemail',
            name='schedule',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='schedule_for_mis_report', to='reporting.CeleryScheduleTask'),
        ),
    ]
