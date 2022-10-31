# Generated by Django 4.0.6 on 2022-10-19 11:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='about/%Y/%m/%d')),
                ('name', models.CharField(max_length=100)),
                ('about_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]