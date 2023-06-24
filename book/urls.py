from django.urls import path

from .views import catalog

app_name = 'book'
urlpatterns = [
    path('book/', catalog, name='book'),

]
