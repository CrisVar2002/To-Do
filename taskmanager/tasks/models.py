from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Por realizar'),
        ('in_progress', 'En tránsito'),
        ('completed', 'Completada'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return self.title