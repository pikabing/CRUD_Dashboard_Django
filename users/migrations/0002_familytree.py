# Generated by Django 2.1.5 on 2019-06-30 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FamilyTree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parentid', models.CharField(max_length=20)),
                ('childid', models.CharField(max_length=20)),
                ('relation', models.CharField(default='', max_length=10)),
            ],
        ),
    ]