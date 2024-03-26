# urls.py (in your project's main directory)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('quiz/', include('quiz.urls', namespace='quiz')),  # Define the namespace for the quiz app
]
