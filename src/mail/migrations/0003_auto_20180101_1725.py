# Generated by Django 2.0 on 2018-01-01 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0002_auto_20171221_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='size',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='client_ip',
            field=models.GenericIPAddressField(verbose_name='Client IP'),
        ),
        migrations.AlterField(
            model_name='message',
            name='from_address',
            field=models.CharField(max_length=255, verbose_name='From'),
        ),
        migrations.AlterField(
            model_name='message',
            name='is_rbl_listed',
            field=models.BooleanField(verbose_name='Is RBL listed'),
        ),
        migrations.AlterField(
            model_name='message',
            name='to_address',
            field=models.CharField(max_length=255, verbose_name='To'),
        ),
    ]