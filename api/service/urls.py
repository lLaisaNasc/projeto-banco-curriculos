from django.urls import path
from .views import user, store, department, curriculos, uploads

urlpatterns = [
    path('login/', user.login, name='login'),
    path('users/', user.list_users, name='list_users'),
    path('users/add/', user.add_user, name='add_user'),
    path('users/edit/<str:username>/', user.edit_user, name='edit_user'),
    path('users/delete/<str:username>/', user.delete_user, name='delete_user'),
    path('users/clone/', user.clone_user, name='clone_user'),
    
    # -- import --
    path('importar-curriculo/', curriculos.import_curriculo, name='import_curriculo'),

    # -- store --
    path('stores/', store.list_stores, name='list_stores'),
    path('stores/add/', store.add_store, name='add_store'),
    path('stores/edit/<int:id>/', store.edit_store, name='edit_store'),
    path('stores/delete/<int:id>/', store.delete_store, name='delete_store'),

    # -- department --
    path('departments/', department.list_departments, name='list_departments'),
    path('departments/add/', department.add_department, name='add_department'),
    path('departments/edit/<int:id>/', department.edit_department, name='edit_department'),
    path('departments/delete/<int:id>/', department.delete_department, name='delete_department'),
    
    # -- curriculos --
    path('curriculos/', curriculos.list_curriculos, name='list_curriculos'),
    path('curriculos/<str:cpf>/', curriculos.get_curriculo, name='get_curriculo'),
    path('curriculos/add/', curriculos.add_curriculo, name='add_curriculo'),
    path('curriculos/edit/<int:cpf>/', curriculos.edit_curriculo, name='edit_curriculo'),
    path('curriculos/delete/<str:cpf>/', curriculos.delete_curriculo, name='delete_curriculo'),

    # -- uploads --
    path('upload/foto/', uploads.upload_foto, name='upload_foto'),
    path('upload/foto/delete/<int:id>/', uploads.delete_foto, name='delete_foto'),
]
