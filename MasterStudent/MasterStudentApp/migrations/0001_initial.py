# Generated by Django 4.1.4 on 2023-01-12 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Master_Name', models.CharField(max_length=40)),
                ('Mobile', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=40)),
                ('Password', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_Name', models.CharField(max_length=40)),
                ('Mobile', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=40)),
                ('Password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Left', models.CharField(max_length=20)),
                ('Operation', models.CharField(max_length=10)),
                ('Right', models.CharField(max_length=10)),
                ('Status', models.BooleanField(default=False)),
                ('Students', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MasterStudentApp.student')),
            ],
        ),
    ]
