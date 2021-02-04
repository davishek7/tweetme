from django.contrib import admin
from django.urls import path,include
from tweets.views import (
    home_view,
    tweet_detail_view,
    tweet_list_view,
    tweet_create_view,
    tweet_delete_view,
    tweet_action_view,
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view),
    path('tweets/',tweet_list_view),
    path('create-tweet/',tweet_create_view),
    path('tweets/<int:tweet_id>',tweet_detail_view),
    path('api/tweets/',include('tweets.urls')),
]
