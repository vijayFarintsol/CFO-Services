# Generated by Django 2.2 on 2021-03-13 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('django_celery_beat', '0014_remove_clockedschedule_enabled'),
        ('import_app', '0008_auto_20210303_1211'),
    ]

    operations = [
        migrations.CreateModel(
            name='MISReportScheduleEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=60, null=True)),
                ('croninput', models.CharField(blank=True, default='0 0 17 ? * SAT *', max_length=70)),
                ('mis_name', models.CharField(blank=True, max_length=40, null=True)),
                ('days', models.CharField(blank=True, max_length=50, null=True)),
                ('is_daily', models.BooleanField(default=False)),
                ('from_email', models.CharField(max_length=90)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='import_app.Company')),
                ('task', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='scheduel_task_for_mis_report', to='django_celery_beat.PeriodicTask')),
            ],
            options={
                'verbose_name': 'MISReportScheduleEmail',
                'verbose_name_plural': 'MISReportScheduleEmail',
                'ordering': ['created_at'],
            },
        ),
    ]
