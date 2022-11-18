from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from employ.api.urls import router
from rest_framework.authtoken import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

openapi_info = openapi.Info(
    title="Simple Inventory API",
    description= "This is a simple API",
    default_version="1.0.0",
    terms_of_service="http://www.apache.org/licenses/LICENSE-2.0.html",
    license=openapi.License(name="Apache 2.0"),
)

schema_view = get_schema_view(
    openapi_info,
    public=True,
    permission_classes=()
)

urlpatterns = [
    # swagger
    re_path(r'^doc(?P<format>\.json|\.yaml)$',schema_view.without_ui(cache_timeout=0), name='schema-json'),  
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'), 
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    # for admin
    path('admin/', admin.site.urls),
    
    # for Token
    path('api/token/', views.obtain_auth_token),
    
    
    # for API
    path('', include(router.urls)),
      
]
