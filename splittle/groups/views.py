from django.shortcuts import get_object_or_404, redirect, render
from .forms import GroupCreationForm
from django.contrib.auth.models import Group, User


def viewGroups(request):
    # Get all groups the logged-in user is part of
    user_groups = request.user.groups.all()
    
    # Pass the user's groups to the template
    return render(request, 'viewGroups.html', {'user_groups': user_groups})

def createGroup(request):
    if request.method == 'POST':
        form = GroupCreationForm(request.POST)
        if form.is_valid():
            # Save the group first
            group = form.save()
            # Add logged in user to group
            group.user_set.add(request.user)
            # Get the usernames field and process it
            usernames = form.cleaned_data.get('usernames')
            if usernames:
                # Split input and trim whitespace
                username_list = [username.strip() for username in usernames.split(',')]
                users = User.objects.filter(username__in=username_list)
                if users.count() < len(username_list):
                    # Handle the case where some usernames are invalid
                    return render(request, "createGroup.html", {
                        'form': form,
                        'error': 'Some usernames are invalid'
                    })
                group.user_set.add(*users)
            return redirect('viewGroups')
    else:
        form = GroupCreationForm()
    
    return render(request, 'createGroup.html', {'form': form})
