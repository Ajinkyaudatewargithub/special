# Generated by Django 3.2.7 on 2022-03-30 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True)),
                ('img', models.URLField(default='', max_length=300)),
                ('text', models.TextField(blank=True)),
                ('date_publish', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True)),
                ('text', models.TextField(default='', max_length=10000)),
                ('topic_tag', models.ManyToManyField(to='app.Topic')),
            ],
        ),
    ]
