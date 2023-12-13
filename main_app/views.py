from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Dog

# Create your views here.

class DogCreate(CreateView):
    model = Dog
    fields = '__all__'

class DogUpdate(UpdateView):
    model = Dog
    fields = ['breed', 'description', 'age']
    
class DogDelete(DeleteView):
    model = Dog
    success_url = '/dogs'


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    # go to db and get all the dogs
    # and store the dogs in a variable called dogs
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', {'dogs': dogs})

# dog_id comes from the path in the urls
# the argument of the function must match the param name
def dogs_detail(request, dog_id):
    # find the cat with id (dog_id) from the database
    dog = Dog.objects.get(id=dog_id)
    
    # 'dog' is the variable name in dogs/detail.html
    # the value of that variable is dog
    return render(request, 'dogs/detail.html', {'dog': dog})