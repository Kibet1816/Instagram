from django.shortcuts import render
from .models import Image
from django.contrib.auth.decorators import login_required

def index(request):
    """
    View function to render the homepage
    """
    return render(request,'all-templates/index.html')

@login_required(login_url='/accounts/login/')
def display_images(request):
    images = Image.all_images()
    return render(request,'all-templates/index.html',{"images":images})