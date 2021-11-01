# Generated by Django 3.2.8 on 2021-10-28 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('number_of_times_viewed', models.PositiveIntegerField(default=0)),
                ('content', models.TextField()),
                ('date_published', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
