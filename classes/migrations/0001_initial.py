# Generated by Django 4.2 on 2023-05-07 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0002_rename_atendance_attendance'),
        ('teachers', '0004_exam_question_examsubmission_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('students', models.ManyToManyField(to='students.student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=10)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('class_obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.class')),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.class')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student')),
            ],
        ),
    ]