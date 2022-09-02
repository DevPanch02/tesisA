from django.urls import path
from core.users.views import listarUsuarios,UserCreateView,UserUpdateView,DeleteView, cambiarPass

app_name = 'users'

urlpatterns = [
    # user

    path('usuario/list-user/', listarUsuarios.as_view(), name='user_list'),
    path('usuario/add-user/', UserCreateView.as_view(), name='user_create'),
    path('usuario/update-user/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('usuario/delete-user/<int:pk>/', DeleteView.as_view(), name='user_delete'),

    path('cambiar/', cambiarPass, name='cambiarPass')

]
