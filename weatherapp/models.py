from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    company_name = models.CharField(max_length=120, blank=True, null=True)
    website = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contact: {self.name} ({self.email})"


class Feedback(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback: {self.name}"
    
class Subscription(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Subscription: {self.email}"


class Camera(models.Model):
    title = models.CharField(max_length=120)             # e.g. "New York"
    country = models.CharField(max_length=80, blank=True) # "USA"
    image = models.ImageField(upload_to="cameras/", blank=True, null=True)
    is_high_quality = models.BooleanField(default=False)
    stream_url = models.URLField(blank=True, null=True)  # optional live stream url
    timestamp = models.DateTimeField(auto_now_add=True)  # when camera was added/updated

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.title} ({self.country})"
