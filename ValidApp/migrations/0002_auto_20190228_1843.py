# Generated by Django 2.2 on 2019-02-28 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ValidApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='year',
            field=models.IntegerField(default='', max_length=4),
        ),
    ]
