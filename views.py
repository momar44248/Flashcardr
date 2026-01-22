import random
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Kanji


# 🏠 Home page (guest + user)
def home(request):
    return render(request, 'home.html')


# 📝 Register page
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Username шалгах
        if User.objects.filter(username=username).exists():
            return render(request, 'registration/register.html', {
                'error': 'Username аль хэдийн байна'
            })

        # User үүсгэх
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # Шууд login хийх
        login(request, user)
        return redirect('home')

    return render(request, 'registration/register.html')


# 🈶 Flashcards (login required)
@login_required
def flashcards(request):
    level = request.GET.get('level')  # N5, N4, N3...
    kanjis = Kanji.objects.filter(level=level) if level else Kanji.objects.all()

    kanji = random.choice(kanjis) if kanjis.exists() else None

    return render(request, 'flashcards/flashcard.html', {
        'kanji': kanji
    })


# 👤 My Account page
@login_required
def account(request):
    return render(request, 'flashcards/account.html')


# 🚪 Logout
def logout_view(request):
    logout(request)
    return redirect('home')