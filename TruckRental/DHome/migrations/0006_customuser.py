# Generated by Django 4.1.2 on 2023-03-05 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DHome', '0005_customerform1_delete_customerform'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUSer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('role', models.CharField(max_length=20)),
            ],
        ),
    ]
