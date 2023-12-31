# Generated by Django 4.2.6 on 2023-10-14 01:01

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
            name='JudgeAppoinments',
            fields=[
                ('appoinment_id', models.AutoField(primary_key=True, serialize=False)),
                ('cnr_number', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Judges',
            fields=[
                ('judge_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('profile_pic', models.ImageField(upload_to='')),
                ('date_of_birth', models.DateField()),
                ('bio', models.TextField()),
                ('case_count', models.IntegerField()),
                ('case_count_priority', models.IntegerField()),
                ('court_name', models.CharField(max_length=100)),
                ('court_type', models.CharField(max_length=50)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JudgeHearing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule', models.DateTimeField()),
                ('end_schedule', models.DateTimeField()),
                ('appoinments_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='judgehandle.judgeappoinments')),
                ('judge_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='judgehandle.judges')),
            ],
        ),
        migrations.CreateModel(
            name='JudgeCalander',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnr_number', models.CharField(max_length=150, unique=True)),
                ('appoinmets_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='judgehandle.judgeappoinments')),
                ('hearing_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='judgehandle.judgehearing')),
            ],
        ),
    ]
