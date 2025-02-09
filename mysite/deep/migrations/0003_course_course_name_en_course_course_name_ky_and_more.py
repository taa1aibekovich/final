# Generated by Django 5.1.4 on 2025-01-13 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deep', '0002_remove_userprofile_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_name_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='course_name_ky',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='course_name_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='description_ky',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='delivery',
            name='feedback_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='delivery',
            name='feedback_ky',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='delivery',
            name='feedback_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='faculty',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='faculty',
            name='description_ky',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='faculty',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='faculty',
            name='faculty_name_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='faculty',
            name='faculty_name_ky',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='faculty',
            name='faculty_name_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='homework',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='homework',
            name='description_ky',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='homework',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='homework',
            name='title_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='homework',
            name='title_ky',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='homework',
            name='title_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='office',
            name='building_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='office',
            name='building_ky',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='office',
            name='building_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='professor',
            name='title_en',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='professor',
            name='title_ky',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='professor',
            name='title_ru',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
