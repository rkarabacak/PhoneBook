# Generated by Django 2.2.6 on 2019-11-12 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0010_auto_20191111_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='companyName',
            field=models.CharField(default=None, max_length=50),
        ),
    ]