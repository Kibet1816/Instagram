from django.shortcuts import render,redirect
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
        