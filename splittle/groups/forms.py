from django import forms
from django.contrib.auth.models import Group, User

class GroupCreationForm(forms.ModelForm):
    usernames = forms.CharField(required=False, help_text="Enter usernames separated by commas")

    class Meta:
        model = Group
        fields = ['name']

    def save(self, commit=True):
        group = super().save(commit=False)
        if commit:
            group.save()

        # Process users if any were provided
        user_names = self.cleaned_data.get('usernames', '')
        user_names = [name.strip() for name in user_names.split(',') if name.strip()]
        for username in user_names:
            try:
                user = User.objects.get(username=username)
                group.user_set.add(user)
            except User.DoesNotExist:
                # Handle the case where a user does not exist
                pass
        return group