# Generated by Django 4.0.4 on 2022-06-13 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0022_student_stimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='CDuration',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='CPrice',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='fee',
            name='Admission',
            field=models.PositiveIntegerField(default=2000),
        ),
        migrations.AlterField(
            model_name='fee',
            name='FAmount',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='fee',
            name='Refundable_Deposit',
            field=models.PositiveIntegerField(default=3000),
        ),
        migrations.AlterField(
            model_name='student',
            name='StPhone',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='TPhone',
            field=models.PositiveIntegerField(),
        ),
    ]