# Generated by Django 2.2.6 on 2019-10-30 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Call_Logs', '0003_auto_20191026_2037'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='call_logs',
            options={'ordering': ['callTime']},
        ),
    ]
