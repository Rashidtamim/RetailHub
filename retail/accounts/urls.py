from django.urls import path

from accounts.views import *

urlpatterns = [
   path('login/' , user_login , name="login" ),
   path('register/' , user_registration , name="register"),
   path('logout/', user_logout, name='logout'),
   path('activate/<email_token>/' , activate_email , name="activate_email"),

]