from django import forms


class VideoForm(forms.Form):
    video_id = forms.IntegerField(label='Video ID', max_value=10000, required=True)
    video_title = forms.CharField(label='Video Title', max_length=50, required=True)
    video_description = forms.CharField(label='Video Description', max_length=100, required=True)
    image_url = forms.CharField(label='Image URL', max_length=200, required=True)

