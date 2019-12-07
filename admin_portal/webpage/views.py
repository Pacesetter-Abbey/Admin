from django.shortcuts import render

posts = [
    {
        'author': 'Abiodun Lawal',
        'title': 'Computer Engineer 1',
        'content': 'Admin Portal Creator',
        'date_posted': 'October 15, 2019'
    },
    {
        'author': 'Caleb Harrison',
        'title': 'Computer Engineer 2',
        'content': 'Admin Link Creator',
        'date_posted': 'October 17, 2019'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'webpage/home.html', context)

def globals(request):
    return render(request, 'webpage/globals.html', {'title': 'Globals'})

def finance(request):
    return render(request, 'webpage/finance.html')

def sales(request):
    return render(request, 'webpage/sales.html')

def hr(request):
    return render(request, 'webpage/hr.html')

def engineering(request):
    return render(request, 'webpage/engineering.html')

