from django.db import models
from django.contrib.auth.models import User, Group

class Bill(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='bills')
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    bill_type = models.CharField(max_length=255)  # Added bill type (e.g., grocery, rent, etc.)
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.amount} for {self.group.name}"

class BillItem(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.price} on {self.bill.name}"

class ItemUserShare(models.Model):
    item = models.ForeignKey(BillItem, on_delete=models.CASCADE, related_name='user_shares')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    share_percentage = models.DecimalField(max_digits=5, decimal_places=2)  # e.g., 0.5 for 50%

    def __str__(self):
        return f"{self.user.username} has {self.share_percentage * 100}% of {self.item.name}"

class UserBill(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name='user_bills')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount_owed = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user.username} owes {self.amount_owed} for {self.bill.name}"


class UserBillItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(BillItem, on_delete=models.CASCADE)
    amount_owed = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user.username} owes {self.amount_owed} for {self.item.name}"