"""
URL configuration for data_analysis_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        'message': 'AI Data Analysis API',
        'version': '1.0.0',
        'endpoints': {
            'datasets': '/api/datasets/',
            'analyses': '/api/analyses/',
            'visualizations': '/api/visualizations/',
            'auth': {
                'signup': '/api/auth/signup/',
                'signin': '/api/auth/signin/',
                'signout': '/api/auth/signout/',
                'profile': '/api/auth/profile/'
            }
        }
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api_root'),
    path('api/', include('analytics.urls')),
    path('api/', include('authentication.urls')),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
