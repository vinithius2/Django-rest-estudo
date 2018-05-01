# Generated by Django 2.0.4 on 2018-05-01 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('birth', models.DateField()),
                ('adress', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('schooling', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'STUDENT',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('birth', models.DateField()),
                ('adress', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('matter', models.CharField(max_length=150)),
                ('FK_TEACHER_STUDENT', models.ManyToManyField(to='school.Student')),
            ],
            options={
                'db_table': 'TEACHER',
                'ordering': ('name',),
            },
        ),
    ]
