from django.db import models
from django.utils import timezone

from .basedates import BaseDates
from .subject import Subject
from .lineitem import LineItem

class Score(BaseDates):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    lineitem = models.ForeignKey(LineItem, on_delete=models.CASCADE)
    activity_progress = models.CharField(max_length=20, null=True, choices=[('Initialized', 'Initialized'), ('Started', 'Started'), ('InProgress', 'InProgress'), ('Submitted', 'Submitted'), ('Completed', 'Completed')], blank=True)
    grading_progress = models.CharField(max_length=20, null=True, choices=[('FullyGraded', 'FullyGraded'), ('Pending', 'Pending'), ('PendingManual', 'PendingManual'), ('Failed', 'Failed')], blank=True)
    score_given = models.FloatField(null=True, blank=True)
    score_maximum = models.FloatField(null=True, blank=True)
    comment = models.CharField(max_length=200, null=True, blank=True)

    def set_grading_progress(self, new_status):
        self.grading_progress = new_status

    def set_activity_progress(self, new_status):
        self.activity_progress = new_status

    class Meta:
        unique_together = [
            ['subject', 'lineitem'],
        ]

