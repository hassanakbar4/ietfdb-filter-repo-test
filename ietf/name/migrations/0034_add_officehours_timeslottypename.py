# Generated by Django 2.2.19 on 2021-03-29 08:28

from django.db import migrations


def forward(apps, schema_editor):
    TimeSlotTypeName = apps.get_model('name', 'TimeSlotTypeName')
    
    TimeSlotTypeName.objects.get_or_create(
        slug='officehours',
        defaults=dict(
            name='Office Hours',
            desc='Office hours timeslot',
            used=True,
        )
    )

def reverse(apps, schema_editor):
    pass  # don't remove the name when migrating

class Migration(migrations.Migration):

    dependencies = [
        ('name', '0033_populate_agendafiltertypename'),
    ]

    operations = [
        migrations.RunPython(forward, reverse),
    ]
