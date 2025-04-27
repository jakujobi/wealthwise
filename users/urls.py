from django.urls import path
from .views import profile, login_view, logout_view, register, edit_profile, account_settings, delete_account, payment, forgot_password, verify_otp, reset_password, change_password

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile, name='profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('account_settings/', account_settings, name='account_settings'),
    path('delete_account/', delete_account, name='delete_account'),
    path('payment/', payment, name='payment'),
    path('forgot_password/', forgot_password, name='forgot_password'),
    path('verify_otp/', verify_otp, name='verify_otp'),
    path('reset_password/', reset_password, name='reset_password'),
    path('change_password/', change_password, name='change_password'),
]