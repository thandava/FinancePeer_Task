from django.urls import path
from django.views.generic import TemplateView
from account import views

app_name='account'

urlpatterns = [
	#path('', TemplateView.as_view(template_name="account/index.html")),
	path('login',views.user_login,name='user_login'),
	path('upload', views.SaveData),
	path('show', views.show),
	path('logout', views.user_logout, name='logout'),
	path('register',views.register,name='register'),
]