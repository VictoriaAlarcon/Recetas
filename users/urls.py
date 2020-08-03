from django.urls import path
from users import views

"""Rutas de usuario"""
urlpatterns = [
    path(route='login/', view=views.login_view, name='login'),
    path(route='logout/', view=views.logout_view, name='logout'),
    path(route='registrar/', view=views.add_user, name='registrar'),
    path(route='profile/', view=views.update_profile, name='profile'),
    path(route='superuser/', view=views.add_superuser, name='superuser'),
]
