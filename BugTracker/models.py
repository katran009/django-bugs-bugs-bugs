"""
BugTicket:
Title
Time/Date Field
Description
Name of user who filed ticket
Status of Ticket (Choices= New/In Progress/Done/Invalid)
Name of user assigned to ticket
Name of user who completed ticket
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class BugTicket(models.Model):
    NEW = 'N'
    IN_PROGRESS = 'IP'
    DONE = 'D'
    INVALID = 'IV'
    STATUS_CHOICES = [
        (NEW, 'New'),
        (IN_PROGRESS, 'In Progress'),
        (DONE, 'Done'),
        (INVALID, 'Invalid')
    ]
    ticket_author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    post_time = models.DateTimeField(default=timezone.now)
    ticket_status = models.CharField(
        max_length=2, choices=STATUS_CHOICES, default=NEW)
    assigned_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='assigned_user',
        default=None,
        null=True,
    )
    finished_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='finished_user',
        default=None,
        null=True,
    )

    def __str__(self):
        return f'{self.post_time} - {self.ticket_author}'
