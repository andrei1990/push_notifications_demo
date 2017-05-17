from django.shortcuts import render,redirect
from push_demo.videos.models import Video
from .forms import VideoForm
from django.views.decorators.csrf import csrf_exempt


def index(request):
    context = {'data_context': 'This is  rendered from the video template'}
    return render(request, 'videos/index.html', context)


@csrf_exempt
def video_form(request):
    # if this is a POST request we process the form data
    if request.method == 'POST':
        print('is a form')
        # create a form instance and populate it with data from the request:
        form = VideoForm(request.POST)
        print('the data from the form', form)
        # check if  it's valid:
        if form.is_valid():
            Video.objects.update_or_create(video_id=form.cleaned_data["video_id"],
                                           video_title=form.cleaned_data["video_title"],
                                           video_description=form.cleaned_data["video_description"],
                                           image=form.cleaned_data["image_url"])
            form = VideoForm()
            # return redirect('videos/index.html')

    # if a GET (or any other method) create a blank form
    else:
        form = VideoForm()
    return render(request, 'videos/form.html', {'form': form})
