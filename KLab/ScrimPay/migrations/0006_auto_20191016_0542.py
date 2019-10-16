# Generated by Django 2.2.6 on 2019-10-16 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ScrimPay', '0005_auto_20191011_0836'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='billing_date',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='cancellation_url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='free_trial_period',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='is_download',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='is_rental',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='is_student_discount',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='service_detail',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='works_num',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
