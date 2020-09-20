from django.forms import ModelForm
from .models import QuizSource

# Custom user forms here
class CreateUserForm(ModelForm):
    class Meta:
        model = QuizSource
        fields = ['quiz', 'degree']
