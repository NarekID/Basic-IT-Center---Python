from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = "blog"

urlpatterns = [
    # path('', views.post_list, name="post_list"),
    path('<int:y>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name="post_detail"),
    # path('hello/', views.HelloClassView.as_view()),
    path('', views.PostListView.as_view(), name="post_list"),
    path('<int:post_id>/share/', views.post_share, name="post_share"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
