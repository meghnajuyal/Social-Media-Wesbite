# Generated by Django 3.0.3 on 2020-06-23 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_auto_20200624_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cr_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
