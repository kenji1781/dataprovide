# Generated by Django 3.2.4 on 2021-08-06 00:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20210806_0924'),
    ]

    operations = [
        migrations.RenameField(
            model_name='machine_data',
            old_name='gus_usage',
            new_name='gas_usage',
        ),
    ]
