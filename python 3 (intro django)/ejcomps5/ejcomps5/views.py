from django.shortcuts import render

def menuView(request):
    return render(request, 'menu.html')