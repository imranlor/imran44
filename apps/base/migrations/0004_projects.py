# Generated by Django 5.0 on 2023-12-08 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_services'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='название')),
                ('description', models.CharField(max_length=500, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'почетная доска',
                'verbose_name_plural': 'почетная доска',
            },
        ),
    ]
