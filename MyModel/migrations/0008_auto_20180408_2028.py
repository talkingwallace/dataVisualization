# Generated by Django 2.0.2 on 2018-04-08 12:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MyModel', '0007_auto_20180408_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('created_time', models.DateTimeField()),
                ('data_type', models.CharField(choices=[('T', 'txt'), ('D', 'database')], max_length=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='datasource',
            name='data_type',
            field=models.CharField(choices=[('T', 'txt'), ('D', 'database')], max_length=1),
        ),
        migrations.AlterUniqueTogether(
            name='dataset',
            unique_together={('name', 'user')},
        ),
    ]
