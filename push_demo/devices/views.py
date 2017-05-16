from django.views.decorators.csrf import csrf_exempt
from push_notifications.models import GCMDevice
from push_demo.videos.models import Video
from django.core import serializers
from django.shortcuts import render
from django.db.models.signals import post_save
from django.dispatch import receiver
# from django.shortcuts import get_object_or_404
# from django.forms.models import model_to_dict

# csrf_exempt decorator is used to disable CSRF protection for this view
@csrf_exempt
def index(request):
    if request.method == 'POST':
        token = request.POST['token']
        # list of all the registered devices
        registered_devices = [device["registration_id"] for device in GCMDevice.objects.values('registration_id')]
        print(type(registered_devices))
        if token not in registered_devices:
            # create new entry in the DB
            GCMDevice.objects.create(registration_id=token, cloud_message_type="FCM")
    return render(request, 'devices/index.html')

# observer that tracks is the Video model has new entries
# in the case of a new entry all the registered devices are getting notified
@receiver(post_save, sender=Video)
def observe_video(sender, **kwargs):
    registered_devices = [device['registration_id'] for device in GCMDevice.objects.values('registration_id')]
    latest_video = [Video.objects.latest('created_at')]
    video_content = serializers.serialize('json', latest_video)
    for device_id in registered_devices:
        fcm_device = GCMDevice.objects.get(registration_id=device_id)
        fcm_device.send_message(video_content)
    print ('Notification was sent to the registered devices')