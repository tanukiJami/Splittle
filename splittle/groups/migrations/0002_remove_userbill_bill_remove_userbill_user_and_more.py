# Generated by Django 5.1.1 on 2024-09-15 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userbill',
            name='bill',
        ),
        migrations.RemoveField(
            model_name='userbill',
            name='user',
        ),
        migrations.DeleteModel(
            name='Bill',
        ),
        migrations.DeleteModel(
            name='UserBill',
        ),
    ]
