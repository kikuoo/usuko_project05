# Generated by Django 5.1.1 on 2024-09-27 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SafetyDiary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('site_name', models.CharField(max_length=100)),
                ('contractor_name', models.CharField(max_length=100)),
                ('work_description', models.TextField()),
                ('planned_personnel', models.IntegerField()),
                ('actual_personnel', models.IntegerField()),
                ('safety_notes', models.TextField()),
            ],
        ),
    ]
