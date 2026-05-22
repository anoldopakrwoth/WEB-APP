from django.db import models
from django.contrib.auth.models import User

# Create your models here


class ProduceListing(models.Model):
    #link to a django user(the farmer/seller)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')

    title = models.CharField(max_length=200, help_text="e.g., Organic sweet potatoes, Fresh Tomatoes")
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="price in local currency")
    quantity = models.CharField(max_length=50, help_text="e.g., 50kg bag, 1 crate")
    image = models.ImageField(upload_to='listings/', null=True, blank=True, help_text="Upload a photo of your produce")

    # geography fields to bridge the gap

    village_origin = models.CharField(max_length=100, help_text="village where the produce is located")
    target_town = models.CharField(max_length=100, help_text="nearest town")

    # timestamp when the listing was created
    created_at = models.DateTimeField(auto_now_add=True, help_text="Creation timestamp")
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} - {self.village_origin} to {self.target_town}"

    class Meta:
        ordering = ['-created_at']
