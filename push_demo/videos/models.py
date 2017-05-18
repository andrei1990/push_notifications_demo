from django.db import models
# from django.shortcuts import get_object_or_404


class Video(models.Model):
    video_id = models.IntegerField(default=0)
    video_title = models.CharField(max_length=60)
    video_description = models.CharField(max_length=200)
    image = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s %s' % (self.video_id, self.video_title, self.video_description)

    # the definition of the CRUD is not necessary as we cand use object manager provided by django

    # def create(self, video_id, title, desc):
    #     new_video = Video(video_id=video_id, video_title=title, video_description=desc)
    #     new_video.save()
    #
    # def read(self, video_id):
    #     video = Video.objects.get(video_id)
    #     return video
    #
    # def delete(self, video_id):
    #     video = get_object_or_404(Video.objects.get(video_id))
    #     video.delete()

    # def update_video(title, **kwargs):
    #     video = Video.objects.get(**kwargs)
    #     video.video_title = title
    #     video.save()