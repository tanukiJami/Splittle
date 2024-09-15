from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import Bill, BillItem, UserBill, UserBillItem
from .forms import BillForm, BillItemForm
from django.forms import modelformset_factory
from django.db.models import Sum

# Create your views here.
@login_required
def bills(request, group_id):
    group = Group.objects.get(id=group_id)
    bills = Bill.objects.filter(group=group)
    
    return render(request, 'bills.html', {
        'bills': bills,
        'group': group,
    })

def create_bill(request, group_id):
    BillItemFormSet = modelformset_factory(BillItem, form=BillItemForm, extra=1)
    
    if request.method == 'POST':
        bill_form = BillForm(request.POST)
        item_formset = BillItemFormSet(request.POST)
        
        if bill_form.is_valid() and item_formset.is_valid():
            bill = bill_form.save(commit=False)
            bill.group_id = group_id
            bill.save()
            total_amount = 0

            # Save the items
            for form in item_formset:
                if form.cleaned_data:  # Skip empty forms
                    item = form.save(commit=False)
                    item.bill = bill
                    item.save()
                    total_amount += item.price

            bill.amount = total_amount
            bill.save()

            return redirect('assign_users_to_items', bill_id=bill.id)

    else:
        bill_form = BillForm()
        item_formset = BillItemFormSet(queryset=BillItem.objects.none())

    return render(request, 'create_bill.html', {
        'bill_form': bill_form,
        'item_formset': item_formset,
    })

def bill_details(request, group_id, bill_id):
    bill = get_object_or_404(Bill, id=bill_id, group_id=group_id)
    items = BillItem.objects.filter(bill=bill)
    group = get_object_or_404(Group, id=group_id)
    
    if request.method == 'POST':
        item_form = BillItemForm(request.POST)
        if item_form.is_valid():
            item = item_form.save(commit=False)
            item.bill = bill
            item.save()

            # Update the total amount of the bill
            total_amount = sum(item.price for item in BillItem.objects.filter(bill=bill))
            bill.amount = total_amount
            bill.save()

            return redirect('bill_details', group_id=group_id, bill_id=bill_id)
    else:
        item_form = BillItemForm()

    return render(request, 'bill_details.html', {
        'bill': bill,
        'items': items,
        'item_form': item_form,
        'group': group,
    })

def get_user_amount_for_bill(user, bill, user_count):
    # Example logic assuming the bill amount is split equally among users
    return bill.amount / user_count
