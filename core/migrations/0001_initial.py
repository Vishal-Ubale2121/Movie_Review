# Generated by Django 2.0.2 on 2019-06-26 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=20)),
                ('name2', models.CharField(max_length=100)),
                ('name3', models.CharField(max_length=100)),
                ('name4', models.CharField(max_length=100)),
                ('name5', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'mood',
            },
        ),
    ]
