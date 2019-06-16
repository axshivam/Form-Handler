from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url('app',views.introduction,name=''),
    url('db',views.index1,name=''),
    #Authentication creativity
    url('login/',views.user_login,name="user_login"),
    url('success/',views.success,name="user_success"),
    url('logout/',views.user_logout,name="user_logout"),

]
