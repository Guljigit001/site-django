from django.urls import path
from . import views


app_name = 'blogger'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('blogger-list/', views.PostListView.as_view(), name='blogger_post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('tag/<slug:tag_slug>/',views.post_list, name='post_list_by_tag'),
]
