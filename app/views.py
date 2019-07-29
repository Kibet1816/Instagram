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

def profile(request,username):
    profile = User.objects.get(username=username)
    # print(profile.id)
    try:
        profile_details = Profile.get_by_id(profile.id)
    except:
        profile_details = Profile.filter_by_id(profile.id)
    images = Image.get_profile_images(profile.id)
    title = f'@{profile.username} Instagram photos and videos'

    return render(request, 'profile/profile.html', {'title':title, 'profile':profile, 'profile_details':profile_details, 'images':images})

@login_required(login_url='/accounts/login/')
def profile_image(request):
    if request.method == 'POST':
        images = Image.all_images()
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            pic = form.save(commit=False)
            pic.profile = request.user
            pic.save()
            return redirect('profile' ,username=request.user)
    else:
        form = ImageForm()
    return render(request,'all-templates/profile.html',{"form":form,"images":images})
        