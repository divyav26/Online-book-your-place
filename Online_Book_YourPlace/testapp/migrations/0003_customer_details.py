# Generated by Django 2.2.22 on 2021-12-12 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20211205_1652'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=100)),
                ('customer_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('date', models.DateField()),
            ],
        ),
    ]
