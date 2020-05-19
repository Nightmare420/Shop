# Generated by Django 3.0.6 on 2020-05-19 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20200519_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('ACC', 'accessories'), ('MOBILE', 'mobile'), ('COMPUTERS', 'computers'), ('LAPTOP', 'laptop')], default='mobile', max_length=20),
        ),
    ]