# Generated by Django 4.0.4 on 2022-05-22 19:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stackholders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('due_date', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('course_code', models.CharField(max_length=64)),
                ('dept', models.CharField(max_length=20)),
                ('section', models.CharField(max_length=20)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('faculty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='stackholders.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission_status', models.BooleanField(default=False)),
                ('submission_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('assignment_file', models.FileField(upload_to='uploads/')),
                ('grade', models.IntegerField()),
                ('assignment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='course.assignment')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='stackholders.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
            ],
        ),
        migrations.AddField(
            model_name='assignment',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course'),
        ),
    ]
