# Generated by Django 2.2.6 on 2019-11-12 10:40

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0012_auto_20191112_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='address',
            field=models.TextField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='companyName',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='phoneNumber2',
            field=phone_field.models.PhoneField(blank=True, max_length=31, null=True),
        ),
    ]
