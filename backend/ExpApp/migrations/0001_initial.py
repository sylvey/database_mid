# Generated by Django 3.2.6 on 2021-11-11 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('UserApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('org_id', models.AutoField(primary_key=True, serialize=False)),
                ('org_name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('website', models.URLField(blank=True, null=True)),
            ],
            options={
                'unique_together': {('org_name', 'email', 'website')},
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('place_id', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('pos_id', models.AutoField(primary_key=True, serialize=False)),
                ('pos_name', models.CharField(max_length=100)),
                ('salary', models.IntegerField(blank=True, null=True)),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PosInOrg', to='ExpApp.organization')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PosInPlace', to='ExpApp.place')),
            ],
            options={
                'unique_together': {('pos_name', 'org', 'place', 'salary')},
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('exp_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('pos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ExpOfPos', to='ExpApp.position')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ExpOfUser', to='UserApp.user')),
            ],
        ),
    ]
