# Generated by Django 4.0.4 on 2022-06-13 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0021_alter_fee_options_course_created_student_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='StImage',
            field=models.ImageField(blank=True, default='avatar.jpg', null=True, upload_to=''),
        ),
    ]