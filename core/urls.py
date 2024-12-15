from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Correct import for views from vege app
import vege.views as views  # Ensure the import is correct

urlpatterns = [
    path('receipes/', views.receipes, name="receipes"),
    path('admin/', admin.site.urls),
    path('delete_receipe/<id>/', views.delete_receipe, name='delete_receipe'),
    path('update_receipe/<id>/', views.update_receipe, name='update_receipe'),
]

# Add media files handling in debug mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Add static files handling
urlpatterns += staticfiles_urlpatterns()
