# Generated by Django 5.1.5 on 2025-01-17 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.IntegerField(max_length=10)),
                ('email', models.EmailField(max_length=100)),
                ('course', models.CharField(max_length=200)),
            ],
        ),
    ]
