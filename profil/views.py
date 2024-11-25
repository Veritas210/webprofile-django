from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import MyProject, GuestBook
from .forms import GuestBookForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def my_projects(request):
    projects = MyProject.objects.all()
    return render(request, 'my_projects.html', {'projects': projects})

def guest_book(request):
    if request.method == 'POST':
        form = GuestBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('guest_book')
    else:
        form = GuestBookForm()
    
    guest_entries = GuestBook.objects.all().order_by('-created_at')
    return render(request, 'guest_book.html', {'form': form, 'guest_entries': guest_entries})