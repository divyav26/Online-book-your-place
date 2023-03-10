# Generated by Django 2.2.22 on 2021-12-12 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0005_auto_20211212_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='billing_address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='message',
            field=models.TextField(default='this is a default message.'),
        ),
        migrations.AddField(
            model_name='customer',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
