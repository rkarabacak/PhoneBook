# Generated by Django 2.2.6 on 2019-10-21 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='companyName',
            field=models.CharField(max_length=50),
        ),
    ]