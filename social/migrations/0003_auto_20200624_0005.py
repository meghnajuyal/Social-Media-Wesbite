# Generated by Django 3.0.3 on 2020-06-23 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_auto_20200621_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='uploaded_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='social.Profile'),
        ),
    ]