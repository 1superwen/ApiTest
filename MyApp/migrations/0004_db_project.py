# Generated by Django 3.1.6 on 2021-02-22 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0003_db_home_href'),
    ]

    operations = [
        migrations.CreateModel(
            name='DB_project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('remark', models.CharField(max_length=100, null=True)),
                ('user', models.CharField(max_length=15, null=True)),
                ('other_user', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
