# views.py
from django.shortcuts import render, redirect
from bills.models import BillItem, ItemUserShare, UserBill
from .forms import ItemUserShareForm
from django.forms import modelformset_factory

def assign_users_to_items(request, bill_id):
    item_shares = {}
    items = BillItem.objects.filter(bill_id=bill_id)

    for item in items:
        item_shares[item] = modelformset_factory(ItemUserShare, form=ItemUserShareForm, extra=1)(
            queryset=ItemUserShare.objects.filter(item=item)
        )

    if request.method == 'POST':
        all_valid = True

        for item, formset in item_shares.items():
            if not formset.is_valid():
                all_valid = False

        if all_valid:
            total_amounts = {}
            bill = items[0].bill

            # Process each item's user shares
            for item, formset in item_shares.items():
                item_total_price = item.price

                for form in formset:
                    if form.cleaned_data:
                        user_share = form.save(commit=False)
                        user_share.item = item
                        user_share.save()

                        # Update each user's owed amount
                        user = user_share.user
                        share_percentage = user_share.share_percentage

                        if user not in total_amounts:
                            total_amounts[user] = 0

                        total_amounts[user] += item_total_price * share_percentage

            # Update the UserBill table for each user
            for user, amount in total_amounts.items():
                UserBill.objects.create(bill=bill, user=user, amount_owed=amount)

            return redirect('bill_detail', bill_id=bill_id)

    return render(request, 'assign_users_to_items.html', {
        'item_shares': item_shares,
        'items': items,
    })