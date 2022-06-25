from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from .forms import ProfileForm
from .models import Profile

def indexview(request):
    return render(request, 'photopost/index.html', {})

def photopostview(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            # # newly added
            # caption_name = form.cleaned_data.get('caption_name')
            # profile_image = form.cleaned_data.get('profile_image')
            # profile = Profile(caption_name=caption_name, profile_image=profile_image)
            # profile.save()
            return redirect('success')
    else:
        form = ProfileForm()
    return render(request, 'photopost/home.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')


def searchauthorview(request):
    """ search function  """
    if request.method == "POST":
        query_name = request.POST.get('author_name', None)
        if query_name:
            results = Profile.objects.filter(author_name__contains=query_name)
            print(results)
            return render(request, 'photopost/searchphoto.html', {"results":results})

    return render(request, 'photopost/searchphoto.html')


def searchcaptionview(request):
    """ search function  """
    if request.method == "POST":
        query_name = request.POST.get('caption_name', None)
        if query_name:
            results = Profile.objects.filter(caption_name__contains=query_name)

            return render(request, 'photopost/searchcaption.html', {"results":results})

    return render(request, 'photopost/searchcaption.html')

def photoview(request):
    results = Profile.objects.all()
    return render(request, 'photopost/photoview.html', {"results": results})