# Generated by Django 4.0.4 on 2022-05-21 05:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_alter_lesson_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('rate', models.PositiveSmallIntegerField(default=0)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.lesson')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.lesson')),
            ],
        ),
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('type', models.PositiveSmallIntegerField(choices=[(0, 'like'), (2, 'heart'), (1, 'haha')], default=0)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.lesson')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
