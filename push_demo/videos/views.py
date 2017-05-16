from django.shortcuts import render
from push_demo.videos.models import Video
# from push_notifications.models import GCMDevice
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.core import serializers


def index(request):
    Video.objects.filter(video_id=73839).update(video_title='Everything is the same')
    Video.objects.update_or_create(video_id=4403, video_title='Breaking Bad4', video_description='Breaking Bad full description4')
    context = {'data_context': 'This is  rendered from the template'}
    return render(request, 'videos/index.html', context)

# @receiver(post_save, sender=Video)
# def observe_video(sender, **kwargs):
#     registered_devices = [device["registration_id"] for device in GCMDevice.objects.values('registration_id')]
#     video_content = serializers.serialize('json', Video.objects.all(), fields=('video_id', 'video_title', 'video_description', 'image'))
#     for device_id in registered_devices:
#         fcm_device = GCMDevice.objects.get(registration_id=device_id)
#         fcm_device.send_message(video_content)
#     print ('Message was sent')
