# Generated by Django 5.0.6 on 2024-05-29 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmployID', models.IntegerField()),
                ('EmployName', models.CharField(max_length=50)),
                ('EmployAddress', models.CharField(max_length=50)),
                ('EmploySalary', models.IntegerField()),
            ],
        ),
    ]
