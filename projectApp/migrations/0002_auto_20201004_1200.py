# Generated by Django 3.1 on 2020-10-04 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Book Name')),
                ('description', models.CharField(max_length=255)),
                ('published', models.BooleanField()),
            ],
            options={
                'db_table': 'book',
            },
        ),
        migrations.DeleteModel(
            name='ProjectModel',
        ),
    ]
