# Generated by Django 2.1.7 on 2019-04-19 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shouji',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='yingyong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yname', models.CharField(max_length=30)),
                ('yshouji', models.ManyToManyField(to='demo2.Shouji')),
            ],
        ),
    ]
