# Generated by Django 3.2.4 on 2021-09-05 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20210903_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='machine_data',
            name='input_date',
            field=models.DateField(null=True),
        ),
    ]
