# Generated by Django 4.1.2 on 2022-10-24 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_alter_student_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='students',
        ),
        migrations.RemoveField(
            model_name='student',
            name='parent',
        ),
        migrations.DeleteModel(
            name='Parent',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
