# Generated by Django 2.1.3 on 2018-11-30 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='word',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterUniqueTogether(
            name='word',
            unique_together={('word', 'category')},
        ),
    ]
