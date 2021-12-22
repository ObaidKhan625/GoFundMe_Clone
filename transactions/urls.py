from django.urls import path
from . import views
app_name = 'transactions'

urlpatterns = [
      path('donation-page/<str:pk>/', views.donationPage, name='donation-page'),
      path('transaction-page/<str:pk>/', views.transactionPage, name='transaction-page'),
      path('handlerequest/', views.handlerequest, name='handle-request'),
]