# Generated by Django 3.2.16 on 2022-11-24 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sea_storm_atlas', '0019_stormeventeffect_flooding_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stormevententry',
            name='area_code',
        ),
        migrations.RemoveField(
            model_name='stormevententry',
            name='area_partition',
        ),
    ]
