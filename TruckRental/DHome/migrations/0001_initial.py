# Generated by Django 4.1.2 on 2023-03-05 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dim1', models.IntegerField()),
                ('dim2', models.IntegerField()),
                ('loadWgt', models.IntegerField()),
                ('tadd', models.CharField(max_length=50)),
                ('fadd', models.CharField(max_length=50)),
                ('ddate', models.DateField()),
                ('budg', models.IntegerField()),
                ('desc', models.CharField(max_length=50)),
            ],
        ),
    ]