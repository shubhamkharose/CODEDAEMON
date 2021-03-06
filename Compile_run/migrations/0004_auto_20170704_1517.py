# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-04 09:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Compile_run', '0003_auto_20170704_0548'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_cnt', models.IntegerField(verbose_name=0)),
                ('cpp_session_code', models.CharField(max_length=1000)),
                ('java_session_code', models.CharField(max_length=1000)),
                ('py_session_code', models.CharField(max_length=1000)),
            ],
        ),
        migrations.RemoveField(
            model_name='problem_submission',
            name='problem_id',
        ),
        migrations.RemoveField(
            model_name='problem_submission',
            name='sub_id',
        ),
        migrations.RemoveField(
            model_name='problem_testcase',
            name='problem_id',
        ),
        migrations.RemoveField(
            model_name='problem_testcase',
            name='testcase',
        ),
        migrations.RenameField(
            model_name='problem',
            old_name='problem_sub',
            new_name='success_sub',
        ),
        migrations.RemoveField(
            model_name='user',
            name='cpp_session_code',
        ),
        migrations.RemoveField(
            model_name='user',
            name='java_session_code',
        ),
        migrations.RemoveField(
            model_name='user',
            name='py_session_code',
        ),
        migrations.AddField(
            model_name='problem',
            name='tot_sub',
            field=models.IntegerField(default=0, verbose_name=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='submission',
            name='User',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Compile_run.User'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='submission',
            name='problem_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Compile_run.Problem'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testcase',
            name='problem_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Compile_run.Problem'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Problem_Submission',
        ),
        migrations.DeleteModel(
            name='Problem_TestCase',
        ),
        migrations.AddField(
            model_name='user_problem',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Compile_run.User'),
        ),
        migrations.AddField(
            model_name='user_problem',
            name='problem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Compile_run.Problem'),
        ),
    ]
