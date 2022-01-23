from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from dating_site import settings
from clientapp.custom_auth_token import obtain_auth_token
from clientapp.views import CreateClientAPIView


router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/clients/create/', CreateClientAPIView.as_view()),
    path('api_auth_token/', obtain_auth_token),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
