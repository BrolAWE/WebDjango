# Generated by Django 3.1.4 on 2021-01-03 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dostopr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('rate', models.FloatField()),
                ('photo', models.CharField(max_length=100)),
                ('url', models.CharField(default='null', max_length=200)),
            ],
        ),
    ]
