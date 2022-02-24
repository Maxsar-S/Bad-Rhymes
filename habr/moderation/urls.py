from django.urls import path

import mainapp.views as mainapp
from . import views
from .views import change_moderator_status, ModeratorPage, Ban, Unban

app_name = 'moderation'


urlpatterns = [
    path('moderator_page', ModeratorPage.as_view(), name='moderator_page'),
    path('ban_article/<int:pk>/', Ban, name='ban_article'),
    path('unban_article/<int:pk>/', Unban, name='unban_article'),
    path('change_moderator_status/<int:pk>/', change_moderator_status, name='change_moderator_status'),
    path('ban/<str:model>/<int:pk>', Ban.as_view(), name='ban'),
    path('unban/<int:pk>', Unban.as_view(), name='unban'),
               ]