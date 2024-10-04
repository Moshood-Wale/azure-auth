from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('expense_tracker.urls')),  # Include app-level URLs
    path('', include('social_django.urls', namespace='social')),
]