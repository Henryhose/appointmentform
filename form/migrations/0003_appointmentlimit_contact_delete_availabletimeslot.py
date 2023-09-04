# Generated by Django 4.2.4 on 2023-09-02 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_availabletimeslot_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentLimit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('limit', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('phonenumber', models.CharField(max_length=20)),
                ('place', models.CharField(max_length=100)),
                ('purpose', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('time_slot_choice', models.CharField(choices=[('09:00 – 09:30', '09:00 – 09:30'), ('10:00 – 10:30', '10:00 – 10:30'), ('11:00 – 11:30', '11:00 – 11:30'), ('12:00 – 12:30', '12:00 – 12:30'), ('13:00 – 13:30', '13:00 – 13:30'), ('14:00 – 14:30', '14:00 – 14:30'), ('15:00 – 15:30', '15:00 – 15:30'), ('16:00 – 16:30', '16:00 – 16:30'), ('17:00 – 17:30', '17:00 – 17:30')], max_length=13)),
            ],
        ),
        migrations.DeleteModel(
            name='AvailableTimeSlot',
        ),
    ]
