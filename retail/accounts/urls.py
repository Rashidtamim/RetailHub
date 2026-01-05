from django.urls import path

from accounts.views import *

urlpatterns = [
   path('login/' , user_login , name="login" ),
   path('register/' , user_registration , name="register"),
   path('activate/<email_token>/' , activate_email , name="activate_email"),
]