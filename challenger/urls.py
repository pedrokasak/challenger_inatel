
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from users.api.viewsets import UsersViewSet


router = routers.DefaultRouter()
router.register(r'users', UsersViewSet)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('dashboard/', include('administrative.urls')),
    path('crypto/', include('cryptocurrencyapi.urls')),
    path('import-csv/', include('imports.urls')),

    # API Django Rest Framework
    path('users/api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))  # Django Rest Framework


]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#handler500 = 'administrative.views.handler500'
#handler404 = 'administrative.views.handler404'
