# Generated by Django 2.0.2 on 2018-04-08 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyModel', '0008_auto_20180408_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='data_type',
            field=models.CharField(choices=[('T', 'txt'), ('E', 'excel')], max_length=1),
        ),
    ]