# Generated by Django 3.1.5 on 2021-01-07 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bluestackApp', '0003_auto_20210107_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='firstName',
            field=models.CharField(default='demo', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='lastName',
            field=models.CharField(default='demo', max_length=255),
            preserve_default=False,
        ),
    ]
