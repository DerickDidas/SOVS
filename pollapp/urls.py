from django.urls import path, include
from django.contrib import admin
from pollapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.index, name='index'),  # usijaze chochote hapo kwenye  path('--')ITALETA ERROR
    path('vote/<int:pk>', views.vote, name='vote'),
    path('result', views.result, name='result'),
    path('accounts/', include('accounts.urls'))

]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)