from django.forms import ModelForm
from .models import MyUser

# Custom user forms here
class CreateUserForm(ModelForm):
    class Meta:
        model = MyUser
        fields = ['name', 'email', 'photo']