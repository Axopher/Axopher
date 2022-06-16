# Generated by Django 4.0.4 on 2022-05-02 15:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adminpanel', '0005_delete_course_delete_fee_delete_student_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('TNum', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('TName', models.CharField(max_length=100)),
                ('TAddress', models.CharField(max_length=100)),
                ('TEmail', models.EmailField(max_length=254)),
                ('TDob', models.DateField()),
                ('TPhone', models.IntegerField()),
                ('TQualification', models.CharField(max_length=100)),
                ('TGender', models.CharField(choices=[('M', 'male'), ('F', 'female'), ('O', 'others')], max_length=6)),
            ],
        ),
    ]