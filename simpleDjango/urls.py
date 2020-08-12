#
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path, include
from django.views.generic import RedirectView


def home(request):
    if request.method == 'GET':
        context = {
            'message': "Hello there",
        }
    #    return render(request, 'index.html', context)
    return HttpResponse("Home Page")


def about(request):
    return HttpResponse("About")


urlpatterns = [
    path('', RedirectView.as_view(url='/todo/')),
    path('about/', about),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('todo/', include('todo.urls')),
    path('api/', include('api.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns
