from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    phone=models.CharField(max_length=15,unique=True)

class Task(models.Model):

    PRIORITY_CHOICES = (
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    )

    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("completed", "Completed"),
    )

    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="tasks")

    subject = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    priority = models.CharField(max_length=10,choices=PRIORITY_CHOICES,default="medium")
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default="pending")
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at=models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.title
