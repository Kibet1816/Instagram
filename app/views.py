from django.shortcuts import render
from .models import Image
from django.contrib.auth.decorators import login_required
from .forms import ImageForm

def index(request):
    """
    View function to render the homepage
    """
    return render(request,'all-templates/index.html')

@login_required(login_url='/accounts/login/')
def display_images(request):
    images = Image.all_images()
    return render(request,'all-templates/index.html',{"images":images})

@login_required(login_url='/accounts/login/')
def profile_image(request):
    if request.method == 'POST':
        images = Image.all_images()
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            pic = form.save(commit=False)
            pic.save()
            images = Image.all_images()
    else:
        form = ImageForm()
    return render(request,'all-templates/profile.html',{"form":form,"images":images})
        