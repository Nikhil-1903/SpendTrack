from django.contrib import admin          # It imports Django's built-in Admin Site.
from django.urls import path, include              # This imports the path() function.

from expenses import views                # Use functions from expenses/views.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('expenses/', include("expenses.urls")),
]
