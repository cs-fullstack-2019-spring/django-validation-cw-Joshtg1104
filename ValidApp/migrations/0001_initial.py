# Generated by Django 2.2 on 2019-02-28 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(default='', max_length=60)),
                ('model', models.CharField(default='', max_length=60)),
                ('year', models.DateField()),
                ('mpg', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
