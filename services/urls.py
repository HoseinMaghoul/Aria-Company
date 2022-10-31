from django.urls import path
from . import views


app_name = 'services'


urlpatterns = [
    path('categories/', views.categories, name='categories'),
    path('category/<int:c_id>/', views.category, name='category'),
    path('services/', views.services, name='services'),
    path('service/<int:s_id>', views.service, name='service'),
    
]
