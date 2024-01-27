from django.db import models
from django.utils import timezone

from .baselti import BaseLTI
from .subject import Subject

class Score(BaseLTI):
    grade_book_column_id = models.PositiveIntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    activity_progress = models.CharField(max_length=20, null=True, choices=[('Initialized', 'Initialized'), ('Started', 'Started'), ('InProgress', 'InProgress'), ('Submitted', 'Submitted'), ('Completed', 'Completed')])
    grading_progress = models.CharField(max_length=20, null=True, choices=[('FullyGraded', 'FullyGraded'), ('Pending', 'Pending'), ('PendingManual', 'PendingManual'), ('Failed', 'Failed')])
    score_given = models.FloatField(null=True)
    score_maximum = models.FloatField(null=True)
    comment = models.CharField(max_length=200, null=True)

    def set_grading_progress(self, new_status):
        self.grading_progress = new_status

    def set_activity_progress(self, new_status):
        self.activity_progress = new_status

    class Meta:
        indexes = [
            models.Index(fields=['subject_id', 'grade_book_column_id']),
        ]
        unique_together = [
            ['subject', 'grade_book_column_id'],
        ]

