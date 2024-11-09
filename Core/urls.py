
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('app_users.urls')),
    path('user/contrack/', include('contrack.urls')),
    path('admins/', include('app_users.urls') ),
    path('a/', include('app_users.urls')),
]
