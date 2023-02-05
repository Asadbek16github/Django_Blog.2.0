from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CostomUsers 


class CostomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CostomUsers
        fields = ('username', 'first_name', 'last_name', 'email', 'age', 'birthYear', 'living_country', 'living_city')


class CostomUsersChangeForm(UserChangeForm):
    class Meta:
        model = CostomUsers
        fields = ('first_name', 'last_name', 'email', 'age', 'birthYear', 'living_country', 'living_city')