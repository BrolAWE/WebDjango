# Generated by Django 2.2.1 on 2019-05-29 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_auto_20190424_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='dostopr',
            name='url',
            field=models.CharField(default='null', max_length=200),
        ),
    ]