from .persons.views import PersonViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from api.User.view_user import UserViewSet, Login, Logout


router = DefaultRouter()

router.register(r'Person', PersonViewSet, basename='Person')
# router.register(r'Person-adjudicacion', PersonViewSetAdjudicacion, basename='Person_adjudicacion')

router.register(r'UsersApi', UserViewSet, basename='UsersApi')

urlpatterns = [

    path('', include(router.urls), name="ViewApi"),
     path('Login/', Login.as_view(), name="Login"),
    path('Logout/', Logout.as_view(), name="Logout"),
    
]