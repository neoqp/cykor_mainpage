from phantomapp import views
from django.urls import path
from django.contrib import auth
from django.conf.urls import url
from django.conf.urls import include
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
	url(r'^$',views.index,name="index"),
	url(r'^about/$',views.about,name="about"),
	url(r'^blog/$',views.blog,name="blog"),
	url(r'^blog/post/(\d+)/$',views.blog_post,name="blog_post"),
	url(r'^login/$',LoginView.as_view(template_name="login.html"),name="login"),
	url(r'^logout/$', LogoutView.as_view(), name='logout'),
	url(r'^register/$',views.register,name="register"),
	url(r'^portfolio/$',views.portfolio,name="portfolio"),
	url(r'^users/profile/(?P<username>[a-zA-Z0-9]+)$',views.user_profile,name="user_profile"),
]