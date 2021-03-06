# Generated by Django 3.1.5 on 2021-01-07 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bluestackApp', '0004_auto_20210107_1114'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('bookingMail', models.EmailField(db_index=True, max_length=254, unique=True)),
                ('sitting', models.CharField(max_length=18, null=True)),
                ('currentStatus', models.CharField(blank=True, choices=[('AV', 'Engg Manager'), ('BO', 'Office Manager')], default='AV', max_length=2, null=True)),
            ],
        ),
    ]
