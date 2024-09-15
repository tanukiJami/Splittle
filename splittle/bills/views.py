from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import Bill

# Create your views here.
@login_required
def bills(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    allBills = Bill.objects.filter(group=group)
    return render(request, 'bills.html', {'bills': allBills, 'group': group})