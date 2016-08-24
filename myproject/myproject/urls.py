from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

from django.contrib import admin
from .myapp.views import login
from .myapp.views import home
from .myapp.views import logout
from .myapp.views import viewTag

from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

from django.contrib import admin

# urlpatterns = [
#     url(r'^admin/', include(admin.site.urls)),
#     url(r'^myapp/', include('myproject.myapp.urls')),
#     url(r'^$', login, name='login'),
#     url(r'^home/$', RedirectView.as_view(url='/myapp/list/', name='home',),
#     url(r'^logout/$', logout, name='logout'),
#     url('', include('social.apps.django_app.urls', namespace='social'))
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^myapp/', include('myproject.myapp.urls')),
    url(r'^$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url('', include('social.apps.django_app.urls', namespace='social')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)