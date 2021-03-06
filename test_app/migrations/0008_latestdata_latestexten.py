# Generated by Django 2.0 on 2020-01-14 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0007_entertainexten_polityexten'),
    ]

    operations = [
        migrations.CreateModel(
            name='LatestData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField(blank=True, null=True)),
                ('title', models.CharField(max_length=200)),
                ('url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='LatestExten',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('url', models.TextField()),
            ],
        ),
    ]
