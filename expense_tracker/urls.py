from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from expenses import views

urlpatterns = [
path('admin/', admin.site.urls),
    # Auth
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Your app
    path('', include('expenses.urls')),
path('', include('expenses.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
path("", views.home, name="home"),   # 👈 THIS WAS MISSING
    path("register/", views.register, name="register"),
path('settings/', views.account_settings, name='account_settings'),
path('delete-account/', views.delete_account, name='delete_account'),
    path("accounts/", include("django.contrib.auth.urls")),
# expense_tracker/urls.py
path('account-settings/', views.account_settings, name='account_settings'),
    path(
        'password-change/',
        auth_views.PasswordChangeView.as_view(
            template_name='accounts/password_change.html',
            success_url='/account-settings/'
        ),
        name='password_change'
    ),
path('export-expenses/', views.export_expenses_csv, name='export_expenses'),

]
