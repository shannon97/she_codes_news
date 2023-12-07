from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy, reverse
from .models import NewsStory, Comments
from .forms import StoryForm, CommentsForm
from django.shortcuts import get_object_or_404, redirect


class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = "all_stories"

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
        return context
    
class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        story = self.get_object()
        comments = story.comments.filter(active=True)
        context['newComment'] = comments
        # context['form'] = CommentsForm
        # context['comments'] = Comments.objects
        return context

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyform'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super() .form_valid(form)
    
class EditStoryView(generic.UpdateView):
    form_class = StoryForm
    model = NewsStory
    context_object_name = 'storyform'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def post(self, request, *args, **kwargs):
        if "delete" in request.POST:
            self.get_object().delete()
            return HttpResponseRedirect(reverse('news:index'))
        return super().post(request, *args, **kwargs)


class NewCommentView(generic.CreateView):
    form_class = CommentsForm
    template_name = 'news/comments.html'

    def get(self, request, *args, **kwargs):
        return redirect("news:story", pk=self.kwargs.get("pk"))

    def form_valid(self, form):
        form.instance.author = self.request.user
        story_pk = self.kwargs.get("pk")
        story = get_object_or_404(NewsStory, pk=story_pk)
        form.instance.post = story
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('news:story', kwargs={'pk': self.kwargs.get('pk')})
    