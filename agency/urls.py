from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),                     # Maps to http://127.0.0.1:8000/
    path('services/', views.services_view, name='services'),    # Maps to http://127.0.0.1:8000/services/
    path('work/', views.work_view, name='work'),                # Maps to http://127.0.0.1:8000/work/
    path('about/', views.about_view, name='about'),             # Maps to http://127.0.0.1:8000/about/
    path('contact/', views.contact_view, name='contact'),       # Maps to http://127.0.0.1:8000/contact/
    path('contact/success/', views.success_view, name='success'),
]