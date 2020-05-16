# Generated by Django 3.0.6 on 2020-05-16 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('grade', models.CharField(max_length=20, verbose_name='Grade')),
                ('school', models.CharField(max_length=100, verbose_name='School')),
                ('email', models.EmailField(max_length=254)),
                ('userid', models.CharField(max_length=20, verbose_name='User Id')),
                ('phone', models.CharField(max_length=20)),
                ('registrationDate', models.DateField(auto_now_add=True, verbose_name='Registration Date')),
            ],
        ),
    ]
