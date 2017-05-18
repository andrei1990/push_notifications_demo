from django.views.decorators.csrf import csrf_exempt
from push_notifications.models import GCMDevice, APNSDevice
from push_demo.videos.models import Video
from django.core import serializers
from django.shortcuts import render
from django.db.models.signals import post_save
from django.dispatch import receiver
# from django.shortcuts import get_object_or_404
# from django.forms.models import model_to_dict


# csrf_exempt decorator is used to disable CSRF protection for this view
DEVICE_TYPE = {'APNS': 'ios', 'FCM': 'android'}
@csrf_exempt
def index(request):
    if request.method == 'POST':
        token = request.POST['token']
        device = request.POST['device']
        # list of all the registered devices
        if device == DEVICE_TYPE['APNS']:
            registered_devices_apns = APNSDevice.objects.values_list('registration_id', flat=True)
            if token not in registered_devices_apns:
                # create new entry in the DB
                APNSDevice.objects.create(registration_id=token, name=device)
        elif device == DEVICE_TYPE['FCM']:
            registered_devices_fcm = GCMDevice.objects.values_list('registration_id', flat=True)
            if token not in registered_devices_fcm:
                # create new entry in the DB
                GCMDevice.objects.create(registration_id=token, name=device, cloud_message_type="FCM")
    context_data = list(map(lambda x: x[0:10],  GCMDevice.objects.values_list('registration_id', flat=True)))
    context = {'devices_list': context_data}
    return render(request, 'devices/index.html', context)


# observer that tracks is the Video model has new entries
# in the case of a new entry or update  all the registered devices are getting notified
@receiver(post_save, sender=Video)
def observe_video(sender, **kwargs):
    latest_video = [Video.objects.latest('created_at')]
    video_content = serializers.serialize('json', latest_video)
    fcm_devices = GCMDevice.objects.values_list('registration_id', flat=True)
    #apns_devices =  APNSDevice.objects.values_list('registration_id', flat=True)
    # Sends a notification to one or more registration_ids
    fcm_devices.send_message(video_content)
    #apns_devices.send_message(video_content)
    print ('Notification was sent to the registered devices')