# news/forms.py
from django import forms
from django.forms import ModelForm
from .models import NewsStory, Comments

class StoryForm(ModelForm):
    class Meta:        
        model = NewsStory        
        fields = ['title', 'pub_date', 'content', 'story_image_url', 'story_image']

        labels = {
            'title': 'Title of your story',
            'pub_date': 'Date posted',
            'content': "What's it about?",
            'story_image_url': 'Image URL',
            'story_image': 'Or upload your own '
        }

        widgets = {
            'title': forms.TextInput
            (attrs={'class':'lbl-title', 'placeholder':'Something catchy'}),
            'pub_date': forms.DateInput
            (format='%m/%d/%Y', attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'content': forms.Textarea
            (attrs={'class':'lbl-content', 'placeholder':'Spill that tea hun!'}),
            'story_image_url': forms.URLInput
            (attrs={'class':'lbl-storyImgURL', 'placeholder':'Image Link'}),
            'story_image': forms.FileInput
            (attrs={'class':'lbl-storyImg'})
        }

class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['body']

        labels = { 'body': 'Let us know your thoughts!'}

