# Generated by Django 5.1.5 on 2025-01-26 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_rename_course_course_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_id', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('category', models.CharField(choices=[('In-house', 'In-house'), ('External', 'External')], max_length=20)),
                ('course_id', models.CharField(max_length=20)),
            ],
        ),
    ]
