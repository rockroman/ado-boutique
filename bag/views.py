from django.shortcuts import render

# Create your views here.
def view_bag(request):
    """
    view to render bag content page
    """
    return render(request, 'bag/bag.html')
