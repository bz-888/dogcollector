from django.shortcuts import render

dogs = [
    {'name': 'Amira', 'breed': 'greyhuahua', 'description': 'princess dog', 'age': 7},
    {'name': 'Kiki', 'breed': 'pomchi', 'description': 'sweet little goblin', 'age': 3},
]

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    return render(request, 'dogs/index.html', {'dogs': dogs})