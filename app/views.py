from django.shortcuts import render, redirect
from .models import Image
from django.contrib.auth.decorators import login_required
from .forms import ImageForm


def index(request):
    """
    View function to render the homepage
    """
    return render(request, 'all-templates/index.html')


def homepage(request):
    """
    View function to render the homepage
    """
    return render(request, 'all-templates/home.html')


@login_required(login_url='/accounts/login/')
def display_images(request):
    images = Image.all_images()
    return render(request, 'all-templates/index.html', {"images": images})


@login_required(login_url='/accounts/login/')
def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.save()
    else:
        form = ImageForm()
    return render(request, 'all-templates/upload.html', {'form': form})


@login_required(login_url='/accounts/login/')
def prof(request):
    return render(request, 'all-templates/profile.html')
