# Generated by Django 4.0.4 on 2022-05-23 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_assignment_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='grade',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
