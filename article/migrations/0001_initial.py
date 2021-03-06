# Generated by Django 3.0.4 on 2020-03-27 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name': 'Статью',
                'verbose_name_plural': 'Статьи',
            },
        ),
    ]
