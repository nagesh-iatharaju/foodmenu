from django.urls import path
from .import views
app_name= 'food'
urlpatterns = [
    path('',views.index,name='index' ),
    path('<int:pk>/',views.details.as_view(),name='details'),
    path('add/', views.create_item.as_view(), name='create_item'),
    path('update/<int:id>/',views.update_item,name='update_item'),
    path('delete/<int:id>',views.delete_item,name='delete_item'),
]