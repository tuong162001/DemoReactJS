# Generated by Django 4.0.4 on 2022-05-21 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(default=None, upload_to='courses/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='course',
            name='subject',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterUniqueTogether(
            name='course',
            unique_together={('subject', 'category')},
        ),
    ]