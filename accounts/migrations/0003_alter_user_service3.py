# Generated by Django 4.1.4 on 2022-12-31 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_service3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='service3',
            field=models.CharField(default='.', max_length=200),
        ),
    ]