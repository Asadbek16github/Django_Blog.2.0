from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CostomUsers
from .forms import CostomUserCreationForm, CostomUsersChangeForm

# Register your models here.
class CostomUserAdmin(UserAdmin):
    add_form = CostomUserCreationForm
    form = CostomUsersChangeForm
    model = CostomUsers
    list_display = ['username', 'first_name', 'last_name', 'email', 'age', 'birthYear', 'living_country', 'living_city', 'is_staff']


    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields':('age',)}),
        (None, {'fields':('birthYear',)}),
        (None, {'fields':('living_country',)}),
        (None, {'fields':('living_city',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields':('age',)}),
        (None, {'fields':('birthYear',)}),
        (None, {'fields':('living_country',)}),
        (None, {'fields':('living_city',)}),
    ),

admin.site.register(CostomUsers, CostomUserAdmin)

