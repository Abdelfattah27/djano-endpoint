# Generated by Django 4.1.2 on 2022-10-28 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_remove_student_not starts with m_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='parent',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='parent',
            name='password',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
    ]
