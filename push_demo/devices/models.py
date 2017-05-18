from django.db import models
# from django.shortcuts import get_object_or_404


class Device(models.Model):
    device_id = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % (self.device_id)

    # the definition of the CRUD is not necessary as we can use object manager provided by django
    # def create(self, device_id):
    #     new_device = Device(device_id=device_id)
    #     new_device.save()
    #
    # def read(self, device_id):
    #     device = get_object_or_404(Device.objects.get(device_id))
    #     return device

    # def update(title, **kwargs):
    #     video = Video.objects.get(**kwargs)
    #     video.video_title = title
    #     video.save()

    # def delete(self, device_id):
    #     device = get_object_or_404(Device.objects.get(device_id))
    #     device.delete()

