from django.urls import path
from app1.views import *

urlpatterns = [
    path('', home, name="HOME" ),
    path('creation_blogs', creation_blog, name="CREATION_BLOG"),
    path('pages/', show_blogs, name="BLOGS"),
    path('eliminar/<id>/', eliminar, name="DELETE"),
    path('edit-blog/<id>/', edit_blogs, name="EDIT-BLOG"),
    path('editar-panel/', edit_panel, name="EDIT-PANEL"),
    path('editar/<id>/', editar_user, name="EDIT-USER"),
    path('editar2/<id>/', editar_user2, name="EDIT-USER2"),
    path('pages/<id>', leer_mas, name="LEER_MAS"),
    path('about/', about_me, name="ABOUT_ME"),
    path('eliminar-user/<id>', eliminar_users, name="ELIMINATE-USERS"),
    path('eliminar-blogs/<id>', eliminar_blogs, name="ELIMINATE-BLOGS"),
]
