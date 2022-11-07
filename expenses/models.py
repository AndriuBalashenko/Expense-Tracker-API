from django.db import models
from authentication.models import User


class Expense(models.Model):

    CATEGORY_OPTIONS = [
        ("Self_care", "Self_care"),
        ("Health_and_fitnes", "Health_and_fitnes"),
        ("Cafes_and_restaurants", "Cafes_and_restaurants"),
        ("Car", "Car"),
        ("Education", "Education"),
        ("Recreation_and_entertainment", "Recreation_and_entertainment"),
        ("Payments_commissions", "Payments_commissions"),
        ("Shopping: clothes, appliances", "Shopping: clothes, appliances"),
        ("Products", "Products"),
        ("Directions", "Directions"),
    ]

    category = models.CharField(choices=CATEGORY_OPTIONS, max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2, max_length=200)
    description = models.TextField()
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False)

    class Meta:
        ordering = ["-date"]

    def __str__(self) -> str:
        return str(self.owner) + "'s expenses"
