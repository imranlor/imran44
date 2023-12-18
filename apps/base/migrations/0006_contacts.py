# Generated by Django 5.0 on 2023-12-08 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_rewievs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, verbose_name='почта')),
                ('phone', models.CharField(max_length=255, verbose_name='ТЕЛЕФОН НОМЕР')),
                ('facebook', models.URLField(verbose_name='ссылка от facebook')),
                ('instagram', models.URLField(verbose_name='ссылка от instagram')),
                ('telegram', models.URLField(verbose_name='ссылка от telegram')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
    ]
