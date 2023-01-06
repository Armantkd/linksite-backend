# Generated by Django 4.1.4 on 2023-01-02 01:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('views', models.CharField(max_length=10)),
                ('replies', models.CharField(max_length=10)),
                ('slug', models.SlugField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Rentry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='linkpage.creator')),
            ],
        ),
    ]
