# Generated by Django 4.1.3 on 2022-12-07 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0006_alter_student_clas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('exp', models.IntegerField()),
                ('subject', models.CharField(max_length=10)),
                ('contact', models.CharField(max_length=10)),
            ],
        ),
    ]
