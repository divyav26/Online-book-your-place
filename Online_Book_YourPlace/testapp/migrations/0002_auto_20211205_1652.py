# Generated by Django 2.2.22 on 2021-12-05 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
