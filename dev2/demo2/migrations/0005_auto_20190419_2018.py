# Generated by Django 2.1.7 on 2019-04-19 12:18

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('demo2', '0004_auto_20190419_1755'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='student',
            managers=[
                ('stmage', django.db.models.manager.Manager()),
            ],
        ),
    ]
