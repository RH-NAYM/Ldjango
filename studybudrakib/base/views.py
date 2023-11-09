from django.shortcuts import render



rooms = [
    {'id': 1, 'name': 'Lets learn Python!!!'},
    {'id': 2, 'name': 'Lets Degign'},
    {'id': 3, 'name': 'Developers'},
]


def home(request):
    context = {"rooms":rooms}
    return render(request, 'home.html', context)

def room(request):
    return render(request, 'room.html')

