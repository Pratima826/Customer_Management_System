# Generated by Django 4.1.2 on 2022-10-29 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=40)),
                ('age', models.IntegerField()),
                ('city', models.CharField(max_length=40)),
                ('mobileno', models.CharField(max_length=15)),
            ],
        ),
    ]
