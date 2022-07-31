from django.urls import path
from . import views
from django.contrib import admin

app_name = "links"
path("api/links/", include("links.urls"))
path("active/", ActiveLinkView.as_view(), name=’active_link’)

path("recent/", RecentLinkView.as_view(), name=’recent_link’)

urlpatterns = [
    path("create/", views.PostCreateApi.as_view(), name="api_create"),
    path("update/<int:pk>", views.PostUpdateApi.as_view(), name="api_update"),
    path("delete/<int:pk>", views.PostDeleteApi.as_view(), name="api_delete"),
    path("", views.PostListApi.as_view(), name="api_list"),
]