# Generated by Django 4.0.7 on 2023-03-31 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('overview', models.TextField()),
                ('release_date', models.DateField()),
                ('poster_path', models.CharField(max_length=255)),
            ],
        ),
    ]
