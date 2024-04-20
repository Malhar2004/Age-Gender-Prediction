
from django.urls import path, include
from .views import AgeGenderView, interface
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('agepred/', AgeGenderView.as_view(), name='detect_age_gender'),
    path('', interface, name="interface")
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)