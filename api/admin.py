# users/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import User

from api.models import Article, Comments

'''from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User
'''

'''class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['email', 'username',]'''

admin.site.unregister(User)
admin.site.register(User)
admin.site.register(Article)
admin.site.register(Comments)

