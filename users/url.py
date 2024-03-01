from django.urls import path
from users.views import *
app_name = 'users'

urlpatterns = [
    path('', home_pages_view, name='home'),
    path('service/', xizmatlar_view, name='service'),
    path('frontend/', frontend_view, name='frontend'),
    path('front_register/', front_register_view, name='front_register'),
    path('backend/', backend_view,name='backend'),
    path('backend_register/',backend_register_view,name='backend_register'),
    path('telegram/', telegram_view, name='telegram'),
    path('telegram_register/', telegram_register_view, name='telegram_register'),
    path('smm/', smm_view, name='smm'),
    path('smm_register', smm_register_view, name='smm_register'),
    path('graphic_designer', graphic_view, name='graphic_designer'),
    path('graphic_register', graphic_register_view, name='graphic_register'),
    path('mobil/', mobil_view, name='mobil'),
    path('mobil_register', mobil_register_view, name='mobil_register')
]
