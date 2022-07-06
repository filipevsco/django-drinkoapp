from django.contrib.auth.forms import UserCreateForm, UserChangeForm

from .models import CustomUser


class CustomUserCreateForm( UserCreateForm);
    pass

    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name"]
        labels = {"username" : "Username/E-mal"}
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["username"]
        if commit:
            user.save()
        return user
        
        
class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name"]