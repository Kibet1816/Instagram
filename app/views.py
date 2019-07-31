from django.shortcuts import render, redirect
from .models import Image
from django.contrib.auth.decorators import login_required
from .forms import ImageForm
from django.contrib.auth.models import User
from django.contrib.auth import login


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
def profile(request):
    # profile = User.objects.get(username=username)
    images = Image.all_images()
    return render(request, 'all-templates/profile.html', {'images': images})


@login_required(login_url='/accounts/login/')
def upload_image(request):
    images = Image.all_images()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            # upload.profile = request.user
            upload.save()
            # return redirect('profile', username=request.user)
    else:
        form = ImageForm()
    
    return render(request, 'all-templates/profile.html', {'form':form,'images':images})


@login_required(login_url='/accounts/login/')
def image_upload(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.editor = current_user
            upload.save()
        return redirect('profile')

    else:
        form = ImageForm()
    return render(request, 'all-templates/upload.html', {"form": form})
