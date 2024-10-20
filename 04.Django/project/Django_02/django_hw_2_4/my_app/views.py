from django.shortcuts import render

# Create your views here.
def introduce(request, name):
    context = {
        'name': name,
    }
    return render(request, 'introduce.html', context)