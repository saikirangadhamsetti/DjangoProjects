# Generated by Django 4.1.3 on 2022-12-05 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0003_rename_student1_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='clas',
            field=models.CharField(default='10', max_length=10),
        ),
    ]
