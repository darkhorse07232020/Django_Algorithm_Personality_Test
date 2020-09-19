from django.shortcuts import render, redirect, get_object_or_404
from .models import MyUser 
from .forms import CreateUserForm

# Create your views here.
def create(request):
    form = CreateUserForm(request.POST or None, request.FILES  or None)
    if form.is_valid():
        form.save()
        return redirect("index")
    return render(request, "form.html", {"form": form})

def read(request):
    search_user = request.GET.get('searchuser' or None)

    if search_user:
        users = MyUser.objects.all()
        users = users.filter(name=search_user)
    else:
        users = MyUser.objects.all()
    return render(request, "index.html", {'users': users})

def update(request, id):
    user = get_object_or_404(MyUser, pk=id)
    form = CreateUserForm(request.POST or None, request.FILES or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect("index")
    return render(request, "form.html", {"form": form})


def delete(request, id):
    user = get_object_or_404(MyUser, pk=id)
    form = CreateUserForm(request.POST or None, request.FILES or None, instance=user)
    if request.method == "POST":
        user.delete()
        return redirect("index")
    return render(request, "confirm_delete.html", {"user": user})