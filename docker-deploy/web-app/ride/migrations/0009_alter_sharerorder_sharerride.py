# Generated by Django 4.1.5 on 2023-02-04 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0008_ride_allowsharernum_alter_ride_numpeople_sharerorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharerorder',
            name='sharerride',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sharerride', to='ride.ride'),
        ),
    ]