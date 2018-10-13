from django.contrib import admin
from django.urls import include,path
from django.conf import settings

admin.site.site_header = "Polls"
admin.site.site_title = 'Polls'
urlpatterns = [
    path('polls/',include('polls.urls')),
    path('',include('polls.urls')),
    path('admin/', admin.site.urls),
]
