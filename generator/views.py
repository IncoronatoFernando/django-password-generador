import random
from django.shortcuts import render

# ACA SE DEFINEN LAS RUTAS DE LOS HTML

# Create your views here.
# los request llama al html
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request,'about.html')


def password(request):
    
    characters= list ('abcdefghijklmnopqrstuvwxyz')
    generated_password = ''
    
    length = int(request.GET.get('length')) #<---- con el metodo GET.get se llama al length para que se muetre
    
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('$&=?¡/()+-'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))        
    
    for x in range(length):
        generated_password += random.choice(characters) #<------ con random.choice se seleccionan las listas aleatoriamente
    
    return render(request,'password.html', {'password':generated_password})

    
