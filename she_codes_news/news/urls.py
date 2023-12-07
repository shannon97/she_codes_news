from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newsStory'),
    path('<int:pk>/comments/', views.NewCommentView.as_view(), name='newComment'),
    path('<int:pk>/edit/', views.EditStoryView.as_view(), name='editStory')
]
