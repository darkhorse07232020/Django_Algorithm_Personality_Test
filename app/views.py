from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import QuizSource
from .forms import CreateUserForm

# Create your views here.
def create(request):
    form = CreateUserForm(request.POST or None, request.FILES  or None)
    if form.is_valid():
        form.save()
        return redirect("index")
    return render(request, "form.html", {"form": form})

def read(request):
    search_quiz = request.GET.get(None)

    if search_quiz:
        quiz = QuizSource.objects.all()
        # quiz = users.filter(name=search_quiz)
    else:
        quiz = QuizSource.objects.all()
    quiz = Paginator(quiz, 12)
    page_number = request.GET.get('page')
    page_obj = quiz.get_page(page_number)
    return render(request, "index.html", {'quiz': page_obj})

def update(request, id):
    user = get_object_or_404(QuizSource, pk=id)
    form = CreateUserForm(request.POST or None, request.FILES or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect("index")
    return render(request, "form.html", {"form": form})


def delete(request, id):
    user = get_object_or_404(QuizSource, pk=id)
    form = CreateUserForm(request.POST or None, request.FILES or None, instance=user)
    if request.method == "POST":
        user.delete()
        return redirect("index")
    return render(request, "confirm_delete.html", {"user": user})
