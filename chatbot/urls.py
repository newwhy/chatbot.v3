from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import url

urlpatterns = [
    # Examples:
    # url(r'^$', 'chatbot.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^keyboard/', 'meal.views.keyboard'),
    url(r'^message', 'meal.views.answer'),

]
