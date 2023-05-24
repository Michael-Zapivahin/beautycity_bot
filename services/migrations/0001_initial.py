# Generated by Django 4.1.4 on 2023-05-24 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('phone', models.CharField(max_length=12, verbose_name='Phone')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('phone', models.CharField(max_length=12, verbose_name='Phone')),
                ('photo', models.ImageField(blank=True, max_length=200, null=True, upload_to='', verbose_name='Photo')),
                ('position', models.CharField(max_length=200, verbose_name='Position')),
            ],
        ),
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('cost', models.IntegerField(verbose_name='Cost')),
                ('time', models.IntegerField(blank=True, null=True, verbose_name='Time in minutes')),
            ],
        ),
    ]
