# Generated by Django 3.2.4 on 2021-06-19 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=150)),
                ('publication_year', models.IntegerField()),
                ('author', models.CharField(max_length=100)),
                ('plot', models.TextField()),
            ],
        ),
    ]