# Generated by Django 5.1.4 on 2024-12-05 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_no', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=50)),
                ('expiry_date', models.DateField()),
            ],
        ),
    ]
