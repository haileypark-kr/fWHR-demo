# Generated by Django 2.0.2 on 2019-01-30 12:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(upload_to='')),
                ('gender', models.CharField(max_length=10)),
                ('age', models.IntegerField(default=20)),
                ('fwhr', models.FloatField(default=0.0)),
                ('country', models.CharField(max_length=10)),
            ],
        ),
    ]
