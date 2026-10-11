from django.db import models


class ServiceRequest(models.Model):
    REQUEST_TYPES = [
        ("Towels", "Towels"),
        ("Toiletries", "Toiletries"),
        ("Housekeeping", "Housekeeping"),
        ("Room Service", "Room Service"),
    ]

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("In Progress", "In Progress"),
        ("Complete", "Complete"),
    ]

    room_number = models.CharField(max_length=10)
    request_type = models.CharField(max_length=30, choices=REQUEST_TYPES)
    details = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Room {self.room_number} - {self.request_type}"