from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('mi-vista/', views.Empleados.as_view(), name='mi_vista'),
    path('certificateUsers/', views.EmpleadosCertificados.as_view(), name='certificateUsers'),
    path('auth/', obtain_auth_token),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    
    # ... otras URLs de tu aplicación
]