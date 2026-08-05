from django.db import models
from django.contrib.auth.models import User
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
class Itinerary(models.Model):
    DESTINATIONS = [
        ("India", "India"),
        ("Japan", "Japan"),
        ("Thailand", "Thailand"),
        ("Switzerland", "Switzerland"),
        ("Maldives", "Maldives"),
        ("France", "France"),
        ("Italy", "Italy"),
        ("Norway", "Norway"),
        ("Dubai", "Dubai"),
        ("Bali", "Bali"),
        ("Hawaii", "Hawaii"),
        ("Egypt", "Egypt"),
    ]

    BUDGETS = [
        ("Economy", "Economy"),
        ("Standard", "Standard"),
        ("Luxury", "Luxury"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    destination = models.CharField(
        max_length=50,
        choices=DESTINATIONS
    )

    start_date = models.DateField()

    end_date = models.DateField()

    travelers = models.PositiveIntegerField(default=1)

    budget = models.CharField(
        max_length=20,
        choices=BUDGETS
    )

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.destination}"
    from django.contrib.auth.models import User

class Wishlist(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    destination = models.CharField(max_length=50)

    class Meta:
        unique_together = ("user", "destination")

    def __str__(self):
        return f"{self.user.username} - {self.destination}"
    from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    phone_number = models.CharField(
        max_length=10,
        blank=True
    )

    profile_picture = models.ImageField(
        upload_to="profile_pics/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.user.username