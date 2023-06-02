# Generated by Django 4.1.4 on 2022-12-30 23:52

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('age', models.IntegerField(max_length=2)),
                ('phone', models.CharField(max_length=15)),
                ('country', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
                ('body', models.CharField(max_length=20)),
                ('outcall_price', models.IntegerField(max_length=10)),
                ('incall_price', models.IntegerField(max_length=10)),
                ('service1', models.TextField(blank=True, max_length=100, null=True)),
                ('service2', models.TextField(blank=True, max_length=100, null=True)),
                ('service3', models.TextField(blank=True, max_length=100, null=True)),
                ('service4', models.TextField(blank=True, max_length=100, null=True)),
                ('service5', models.TextField(blank=True, max_length=100, null=True)),
                ('service6', models.TextField(blank=True, max_length=100, null=True)),
                ('service7', models.TextField(blank=True, max_length=100, null=True)),
                ('service8', models.TextField(blank=True, max_length=100, null=True)),
                ('service9', models.TextField(blank=True, max_length=100, null=True)),
                ('service10', models.TextField(blank=True, max_length=100, null=True)),
                ('service11', models.TextField(blank=True, max_length=100, null=True)),
                ('service12', models.TextField(blank=True, max_length=100, null=True)),
                ('service13', models.TextField(blank=True, max_length=100, null=True)),
                ('service14', models.TextField(blank=True, max_length=100, null=True)),
                ('service15', models.TextField(blank=True, max_length=100, null=True)),
                ('service16', models.TextField(blank=True, max_length=100, null=True)),
                ('service17', models.TextField(blank=True, max_length=100, null=True)),
                ('service18', models.TextField(blank=True, max_length=100, null=True)),
                ('service19', models.TextField(blank=True, max_length=100, null=True)),
                ('service20', models.TextField(blank=True, max_length=100, null=True)),
                ('service21', models.TextField(blank=True, max_length=100, null=True)),
                ('about', models.TextField(default='about me', max_length=100)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]