# Generated by Django 2.1.7 on 2019-02-21 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heartbeat', '0002_auto_20190221_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='EXEC_LAST_RUNNING_AT',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
