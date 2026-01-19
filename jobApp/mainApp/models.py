from django.db import models

# Create your models here.

class Product(models.Model):
    State_Denied = 'denied'
    State_Aproved = 'aproved'
    State_Pending = 'pending'

    STATE_CHOICES = [
        (State_Denied, 'denied'),
        (State_Aproved, 'aproved'),
        (State_Pending, 'pending'), 
    ]

    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    role_title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) # Updates time every time the record is saved
    state = models.CharField(
        max_length=10,
        choices=STATE_CHOICES,
        default=State_Pending
    )



    def __str__(self):
        return f"{self.role_title} at {self.company} ({self.get_state_display()})"
