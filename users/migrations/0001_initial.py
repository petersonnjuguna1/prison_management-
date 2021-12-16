# Generated by Django 3.1.7 on 2021-09-06 13:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Prisonerprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=40, null=True)),
                ('username', models.CharField(max_length=40, null=True)),
                ('dob', models.DateField(null=True)),
                ('marital', models.CharField(max_length=10, null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='visitorsprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=40, null=True)),
                ('address', models.CharField(max_length=40, null=True)),
                ('phoneNo', models.CharField(max_length=13, null=True, unique=True)),
                ('date', models.DateTimeField(max_length=40, null=True)),
                ('relationship', models.CharField(max_length=40, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Visitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitationdate', models.DateTimeField(max_length=40, null=True)),
                ('phoneNo', models.CharField(max_length=13, null=True, unique=True)),
                ('status', models.CharField(blank=True, default='Pending', max_length=40, null=True)),
                ('Prisonernumber', models.IntegerField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now=True, max_length=40, null=True)),
                ('prisoner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.prisonerprofile')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('visitor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.visitorsprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Prisonerdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=40, null=True)),
                ('PNo', models.IntegerField(blank=True, null=True)),
                ('offence', models.CharField(max_length=40, null=True)),
                ('sentence', models.IntegerField(null=True)),
                ('datein', models.DateTimeField(max_length=40, null=True)),
                ('dateout', models.DateTimeField(max_length=40, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('prisoner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.prisonerprofile')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]