from django.urls import path
from .views import PowerBIDashboardView, SignUp, HomePageView,pythonDashboardView,loading,python_dashput,loading_put
from django.contrib.auth import views as auth_views
from . import views

app_name = 'Main_app'

urlpatterns =[
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('', HomePageView.as_view(), name='home'),
    path('Python_dashboard/', pythonDashboardView.as_view(), name='python_dashboard'),
    path('python_dashboard_put/', python_dashput.as_view(), name='python_dashboard_put'),
    path('loading/', loading.as_view(), name='loading'),
    path('loading_put/', loading_put.as_view(), name='loading_put'),
    path('PowerBI_dashboard/', PowerBIDashboardView.as_view(), name='powerBI_dashboard'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]