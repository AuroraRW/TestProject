# Generated by Django 3.0.8 on 2021-03-12 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_id', models.IntegerField()),
                ('call_date', models.DateField()),
                ('call_time', models.TimeField()),
                ('result', models.BooleanField()),
            ],
        ),
    ]