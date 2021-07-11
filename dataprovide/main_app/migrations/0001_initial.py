# Generated by Django 3.1.7 on 2021-07-11 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='machine_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_name', models.CharField(max_length=100)),
                ('unit_no', models.IntegerField(default=0)),
                ('ship_date', models.DateField()),
            ],
        ),
    ]
