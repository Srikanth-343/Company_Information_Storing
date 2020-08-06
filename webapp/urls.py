from django.urls import path,include
from . import views
app_name='webapp'

urlpatterns = [
    path('',views.Home, name='Home'),
    path('cform/',views.companyModelView, name='Cform'),
    path('delete/<int:id>/',views.delete_Company, name='deleteComp'),
    path('<int:id>/', views.edit_Company, name='Edit'),

]
