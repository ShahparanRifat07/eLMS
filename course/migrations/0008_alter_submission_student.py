# Generated by Django 4.0.4 on 2022-05-23 02:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stackholders', '0001_initial'),
        ('course', '0007_alter_submission_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stackholders.profile'),
        ),
    ]
