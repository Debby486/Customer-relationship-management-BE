from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('djoser.urls')),

    ## gives a lot of function for example to create users login because of the restframework
    path('api/v1/', include('djoser.urls.authtoken')),
]
