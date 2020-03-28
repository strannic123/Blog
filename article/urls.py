
from django.urls import path

from . import views
from .views import ArticleListView, ArticleDetailView, edit_page

urlpatterns = [

    path('', ArticleListView.as_view(), name='article_list'),
    path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail_list'),
    path('edit-page', views.edit_page, name='edit_page'),
]