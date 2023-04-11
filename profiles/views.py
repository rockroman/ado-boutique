from django.shortcuts import render

# Create your views here.

def profile(request):
    """display users profile"""
    context = {}
    return render(request, 'profiles/profile.html', context)
