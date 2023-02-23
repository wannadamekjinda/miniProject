# Generated by Django 4.1.7 on 2023-02-18 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EducationLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eduLevelName', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facName', models.CharField(default='', max_length=100)),
                ('facDesc', models.TextField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genName', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='LearnGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groName', models.CharField(default='', max_length=30)),
                ('groDesc', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('majorName', models.CharField(default='', max_length=100)),
                ('majorDesc', models.TextField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='MajorProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('majorProName', models.CharField(default='', max_length=100)),
                ('majorProDesc', models.TextField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='StudentStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statusName', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subjectId', models.CharField(default='', max_length=15, primary_key=True, serialize=False)),
                ('subjectName', models.CharField(default='', max_length=50)),
                ('subjectCredit', models.IntegerField(default='1', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacherId', models.CharField(default='', max_length=15, primary_key=True, serialize=False)),
                ('teacherFName', models.CharField(default='', max_length=50)),
                ('teacherLName', models.CharField(default='', max_length=50)),
                ('teacherAddress', models.TextField(default='', max_length=400)),
                ('teacherBirthdate', models.DateField(default=None)),
                ('facName', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='miniApp.faculty')),
                ('gender', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='miniApp.gender')),
                ('major', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='miniApp.major')),
                ('majorProName', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='miniApp.majorprogram')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studentId', models.CharField(default='', max_length=15, primary_key=True, serialize=False)),
                ('studentFName', models.CharField(default='', max_length=50)),
                ('studentLName', models.CharField(default='', max_length=50)),
                ('studentAddress', models.TextField(default='', max_length=400)),
                ('studentBirthdate', models.DateField(default=None)),
                ('eduLevelName', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='miniApp.educationlevel')),
                ('facName', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='miniApp.faculty')),
                ('gender', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='miniApp.gender')),
                ('groName', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='miniApp.learngroup')),
                ('major', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='miniApp.major')),
                ('majorProName', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='miniApp.majorprogram')),
                ('statusName', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='miniApp.studentstatus')),
            ],
        ),
    ]