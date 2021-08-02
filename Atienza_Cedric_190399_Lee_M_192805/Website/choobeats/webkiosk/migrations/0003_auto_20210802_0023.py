# Generated by Django 3.2.5 on 2021-08-01 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webkiosk', '0002_account'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='mobilenumber',
            new_name='number',
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='province',
            field=models.CharField(default=True, max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='customer',
            name='firstname',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='customer',
            name='lastname',
            field=models.CharField(max_length=1000),
        ),
    ]