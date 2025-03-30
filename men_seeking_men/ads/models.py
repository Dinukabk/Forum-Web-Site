from django.db import models

class Ad(models.Model):
    CATEGORY_CHOICES = [
        ('casual', 'Casual'),
        ('dating', 'Dating'),
        ('friendship', 'Friendship'),
        ('other', 'Other'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    contact_info = models.CharField(max_length=100, blank=True, null=True)  # Phone or email
    image = models.ImageField(upload_to='ad_images/', blank=True, null=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)  # Auto-approved ads

    def __str__(self):
        return self.title
