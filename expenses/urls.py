from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('summary/', views.summary, name='summary'),
    path('flask-summary/', views.flask_summary, name='flask_summary'),
    path('account-settings/', views.account_settings, name='account_settings'),
    path('export-expenses/', views.export_expenses_csv, name='export_expenses_csv'),

path('delete-expense/<int:expense_id>/', views.delete_expense, name='delete_expense'),

]


