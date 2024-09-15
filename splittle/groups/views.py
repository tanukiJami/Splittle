from django.shortcuts import get_object_or_404, redirect, render
from .forms import GroupCreationForm
from django.contrib.auth.models import Group, User
from .models import Group, Membership
from django.contrib.auth.decorators import login_required
from django.http import Http404


@login_required
def leaveGroup(request, group_id):
    # Try to get the group object; raise a 404 if not found
    group = get_object_or_404(Group, id=group_id)

    # Find the membership entry for the current user in this group
    membership = Membership.objects.filter(user=request.user, group=group).first()

    # If the membership exists, delete it (user leaves the group)
    if membership:
        membership.delete()
    else:
        raise Http404("You are not a member of this group.")

    # Redirect the user back to the list of groups or homepage
    return redirect('view_groups')

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
