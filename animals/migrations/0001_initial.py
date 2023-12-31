# Generated by Django 4.2.5 on 2023-09-16 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('animal_type', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('breed', models.CharField(max_length=200)),
                ('availability', models.BooleanField()),
                ('description', models.TextField(max_length=500)),
                ('healthy', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Sex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('user', models.IntegerField()),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animals.animal')),
            ],
        ),
        migrations.CreateModel(
            name='AnimalMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_link', models.ImageField(upload_to='animals/images')),
                ('main', models.BooleanField()),
                ('animal_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animals.animal')),
            ],
        ),
        migrations.AddField(
            model_name='animal',
            name='sex',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animals.sex'),
        ),
    ]
