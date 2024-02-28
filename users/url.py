from django.urls import path
from users.views import *
app_name = 'users'

urlpatterns = [
    path('', home_pages_view, name='home'),
    path('service/', xizmatlar_view, name='service'),
    path('telegram/<int:pk>', users_view, name='telegram'),
    path('register/', register_view, name='register'),
    path('veb/<int:pk>', webcite_view, name='veb'),
    path('verify/', verify_code_view, name='verify'),
    path('smm/<int:pk>', smm_view, name='smm'),
    path('graphic_designer/<int:pk>', graph_designer, name='graphic_designer'),
    path('crm/<int:pk>',crm_view,name='crm'),
]
