# Generated by Django 2.0.5 on 2018-05-12 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0024_transportlog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transportlog',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mail.Message'),
        ),
    ]
