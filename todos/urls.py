from django.urls import path
from . import views

urlpatterns=[
    path("", views.index, name="index"),
    path("todos", views.todos, name="todos"),
    path("gots", views.gots, name="gots"),
    path('add/', views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('posts', views.posts, name='posts'),
    path('pandas', views.pandas, name='pandas'),
    path('adddataframe/', views.adddataframe, name='adddataframe'),
    path('adddataframe/adddataframe/', views.adddataframe, name='adddataframe'),
    path('adddataframe/adddataframe/adddataframe/', views.adddataframe, name='adddataframe'),
    path('adddataframe/encoder/', views.encoder, name='encoder'),
]