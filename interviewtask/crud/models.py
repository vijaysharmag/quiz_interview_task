from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _


# Create your models here.


class Employee(TimeStampedModel):
    first_name = models.CharField(_('First name'), max_length=30)
    middle_name = models.CharField(_('Middle name'), max_length=30, blank=True)
    last_name = models.CharField(_('Last name'), max_length=30)
    email = models.EmailField(_('Email address'), unique=True)
    phone_number = models.CharField(_('Phone number'), max_length=12)
    working = models.BooleanField(_('Working'), default=False,
                                  help_text=_('Employee is working in organization or not .'), )

    class Meta:
        ordering = ('-pk',)
        verbose_name = _('Employee')
        verbose_name_plural = _('Employees')

    def __str__(self):
        return self.email


FREQ = (
    ('0.25', '0.25'),
    ('0.5', '0.5'),
    ('1.0', '1.0'),
    ('1.5', '1.5')
    )

INSTRUCTION = (
    ('Before meal', 'Before meal'),
    ('After meal', 'After meal')
)

TIMING = (
    ('Morning', 'Morning'),
    ('Afternoon', 'Afternoon'),
    ('Evening', 'Evening')
)

DURATION = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7')

)

class Dosage(models.Model):
    frequency = models.CharField(max_length=255, choices=FREQ)
    shift = models.CharField(max_length=50, choices=TIMING )

    class Meta:
        db_table = 't_dosage'

class Prescription(TimeStampedModel):
    dosage = models.ForeignKey(Dosage, on_delete=models.CASCADE, related_name='prescription')
    medicine_name = models.CharField(max_length=255)
    duration = models.CharField(max_length=255, choices=DURATION)
    instruction = models.CharField(max_length=255, choices=INSTRUCTION)
    note = models.TextField()
    
    class Meta:
        db_table = 't_prescription'
