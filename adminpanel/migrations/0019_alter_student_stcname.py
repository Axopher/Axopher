# Generated by Django 4.0.4 on 2022-05-16 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0018_remove_student_stcname_student_stcname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='StCName',
            field=models.ManyToManyField(to='adminpanel.course'),
        ),
    ]