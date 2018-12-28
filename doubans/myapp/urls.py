from django.conf.urls import url

from . import views




urlpatterns = [

    url(r'^start/$', views.start, name="start"),
    url(r'^base/$', views.base, name="base"),
    url(r'^home/$',views.home,name="home"),
    url(r'^tuijian/$', views.tuijian, name="tuijian"),
    url(r'^tuijian/(\d+)/$',views.tuijian,name="tuijian"),
    url(r'^mine/$',views.mine,name="mine"),
    url(r'^mine/(\d+)/$',views.mine,name="mine"),
    url(r'^lianxi/$',views.lianxi,name="lianxi"),
    url(r'^like/$',views.like,name="like"),
    url(r'^like/(\d+)/$',views.like,name="like"),
    url(r'^login/$',views.login1,name="login"),
    url(r'^register/$',views.register,name="register"),
    url(r'^loginout/$',views.loginout,name="loginout"),
    url(r'^user_center/$',views.user_center,name="user_center"),
    url(r'^user_center/edit_profile/$', views.edit_profile, name="edit_profile"),
    url(r'^user_center/change_password/$', views.change_password, name="change_password"),










]