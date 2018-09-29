from django.conf.urls import url
from firstapp import views

urlpatterns = [
    url(r'^register/$', views.register_page, name = 'register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^special/$',views.special,name='special'),

]
