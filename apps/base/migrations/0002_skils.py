# Generated by Django 5.0 on 2023-12-08 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skils',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='название')),
                ('percent', models.CharField(max_length=255, verbose_name='процент знании')),
            ],
            options={
                'verbose_name': 'скил',
                'verbose_name_plural': 'скилы',
            },
        ),
    ]