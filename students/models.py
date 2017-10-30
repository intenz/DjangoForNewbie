from django.db import models

# Create your models here.
class Student(models.Model):
    """Student Model"""

    class Meta(object):
        """docstring for Meta."""
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    first_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name='First name')

    last_name= models.CharField(
        max_length=256,
        blank=False,
        verbose_name='Last name')

    middle_name = models.CharField(
        max_length=256,
        blank=True,
        verbose_name='Middle name',
        default='')

    birthday = models.DateField(
        blank=False,
        verbose_name='Birthday',
        null=True)

    photo = models.ImageField(
        blank=True,
        verbose_name='Photo',
        null=True)

    ticket = models.CharField(
        max_length=256,
        blank=False,
        verbose_name='Ticket')

    notes = models.TextField(
        blank=True,
        verbose_name='Notes')

    student_group = models.ForeignKey('Group',
        verbose_name = 'Group',
        blank=False,
        null=True,
        on_delete=models.PROTECT)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

class Group(models.Model):
    """Group Model"""

    class Meta(object):
        """docstring for Meta."""
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'

    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name='Name')

    leader= models.OneToOneField('Student',
        verbose_name='Leader group',
        blank=True,
        null=True,
        on_delete=models.SET_NULL)

    notes = models.TextField(
        blank=True,
        verbose_name='Notes'
    )

    def __str__(self):
        if self.leader:
            return '%s (%s %s)' % (self.title, self.leader.first_name, self.leader.last_name )
        else:
            return '%s' % (self.title)
