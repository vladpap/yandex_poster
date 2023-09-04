from django.shortcuts import render


def map_poster(request):
    return render(request, 'index.html')
