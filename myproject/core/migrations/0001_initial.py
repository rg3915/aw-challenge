# Generated by Django 2.2.1 on 2019-05-12 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Repo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.BigIntegerField(help_text='slug is id of github api', unique=True)),
                ('name', models.TextField()),
                ('full_name', models.TextField()),
                ('htm_url', models.URLField()),
                ('stargazers_count', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ('stargazers_count',),
            },
        ),
    ]