# Generated by Django 2.1.7 on 2019-04-20 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Global_Variables',
            fields=[
                ('VARIABLE_TYPE', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('VARIABLE_VALUE', models.CharField(max_length=500)),
            ],
        ),
    ]
