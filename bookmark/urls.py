from django.urls import path
from .views import *
urlpatterns = [
    # http://127.0.0.1/bookmark/
    # as_view() : 클래스형 뷰를 함수형 뷰로 바꿔줌
    path("", BookmarkListView.as_view(), name='list'),
    path("add/", BookmarkCreateView.as_view(), name='add'),
    path("detail/<int:pk>/", BookmarkDetailView.as_view(), name='detail'),
    path("update/<int:pk>/", BookmarkUpdateView.as_view(), name='update'),
    path("delete/<int:pk>/", BookmarkDeleteView.as_view(), name='delete'),
]