from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('task.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Add this line
    path('', RedirectView.as_view(url='/tasks/')),  # Redirects / to /tasks/
    path('', include('task.urls'))  # Include task URLs at the root
]