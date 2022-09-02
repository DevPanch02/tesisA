"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import handler404, handler500
from core.startpage.views import Error404, Error500
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('core.login.urls'), name='login'),
    path('home/', include('core.startpage.urls'), name='home'),
    path('users/', include('core.users.urls'), name='user'),
    path('report/', include('core.report.urls'), name='report'),


    # api
    path('api/', include('api.urls'), name='api'),

    #   TOKEN API
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404=Error404.as_view()
handler500=Error500.as_view()
