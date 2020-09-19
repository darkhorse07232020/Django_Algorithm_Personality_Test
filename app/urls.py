from django.urls import path
from .views import create, read, update, delete
# Custom urls here
urlpatterns = [
  path('', read, name="index"),
  path('create', create, name="create"),
  path('update/<int:id>', update, name="update"),
  path('delete/<int:id>', delete, name="delete")
]