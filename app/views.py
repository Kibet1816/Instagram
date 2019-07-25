from django.shortcuts import render

def index(request):
    """
    View function to render the homepage
    """
    return render(request,'all-templates/index.html')
