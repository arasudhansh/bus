# Generated by Django 2.2.6 on 2019-12-15 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0006_asehi_date3'),
    ]

    operations = [
        migrations.AddField(
            model_name='passenger',
            name='bus',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bus.Add_Bus'),
        ),
    ]
