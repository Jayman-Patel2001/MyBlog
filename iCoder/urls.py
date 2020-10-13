from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = "iCoder Admin"
admin.site.site_title = "iCoder Admin Panel"
admin.site.index_title = "iCoder Administration"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('blog/', include('blog.urls'))
] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
