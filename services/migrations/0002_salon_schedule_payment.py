# Generated by Django 4.1.4 on 2023-05-24 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('phone', models.CharField(max_length=12, verbose_name='Phone')),
                ('address', models.CharField(max_length=200, verbose_name='Address')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('photo', models.ImageField(blank=True, max_length=200, null=True, upload_to='', verbose_name='Photo')),
                ('lat', models.FloatField(verbose_name='Lat')),
                ('lng', models.FloatField(verbose_name='Lng')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(verbose_name='Date time')),
                ('confirmation', models.BooleanField(default=False, verbose_name='Confirmation')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='schedules', to='services.client', verbose_name='Client')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='schedules', to='services.employee', verbose_name='Employee')),
                ('procedure', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='schedules', to='services.procedure', verbose_name='Procedure')),
                ('salon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='services.salon', verbose_name='Schedule')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debt', models.IntegerField(blank=True, null=True, verbose_name='Debt')),
                ('payment', models.IntegerField(blank=True, null=True, verbose_name='Payment')),
                ('tips', models.IntegerField(blank=True, null=True, verbose_name='Tips')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='payments', to='services.schedule', verbose_name='Order')),
            ],
        ),
    ]
