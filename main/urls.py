from . import views
from django.urls import path

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('causes/', views.causes, name='causes'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('education/', views.education, name='education'),
    path('courses/', views.courses, name='courses'),
    path('courses/schedule', views.schedule, name='schedule'),
    path('single-causes/', views.singlecauses, name='singlecauses'),
    path('donation/', views.donation, name='donation'),
    path('charge/', views.charge, name="charge"),
    path('success/<str:args>/', views.successMsg, name="success"),
    path('register/', views.register, name='register'),
    path('login/', views.loginpage, name='login'),  
    path('logout/', views.logoutUser, name='logout'),


]