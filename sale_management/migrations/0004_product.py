# Generated by Django 3.0 on 2022-04-08 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale_management', '0003_employee_dob'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('price', models.BigIntegerField()),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]