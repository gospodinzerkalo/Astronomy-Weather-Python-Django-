# Generated by Django 2.2.2 on 2019-08-11 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signmenu', '0004_auto_20190807_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeleteUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('password', models.CharField(default='', max_length=30)),
            ],
        ),
    ]
