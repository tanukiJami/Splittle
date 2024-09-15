from django.db import models
# Create your models here.
from django.contrib.auth.models import User, Group

class Bill(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='bills')
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.amount} for {self.group.name}"

class UserBill(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name='user_bills')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount_owed = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user.username} owes {self.amount_owed} for {self.bill.name}"
