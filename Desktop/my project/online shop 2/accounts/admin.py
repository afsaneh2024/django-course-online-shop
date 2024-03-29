

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm,CustomUserCreationForm
from .models import CustomUser

class CustomUsrAdmin(UserAdmin):
    model=CustomUser
    add_form=CustomUserCreationForm
    form=CustomUserChangeForm
    list_display=('email','username', )
    
    
admin.site.register(CustomUser,CustomUsrAdmin)

