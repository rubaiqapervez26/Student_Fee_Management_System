from django.db import models

class FeeRecord(models.Model):
    SEMESTER_CHOICES = [
        ('1st', '1st Semester'), ('2nd', '2nd Semester'),
        ('3rd', '3rd Semester'), ('4th', '4th Semester'),
        ('5th', '5th Semester'), ('6th', '6th Semester'),
        ('7th', '7th Semester'), ('8th', '8th Semester'),
    ]
    STATUS_CHOICES = [('Paid', 'Paid'), ('Unpaid', 'Unpaid')]

    student_name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=50, unique=True)
    semester = models.CharField(max_length=10, choices=SEMESTER_CHOICES, default='1st')
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Unpaid')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student_name} ({self.roll_no})"