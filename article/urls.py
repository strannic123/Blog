
from django.urls import path

from . import views
from .views import ArticleListView, ArticleDetailView, edit_page

urlpatterns = [

    path('', ArticleListView.as_view(), name='article_list'),
    path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail_list'),
    path('edit-page', views.edit_page, name='edit_page'),
    path('update-page/<int:pk>', views.update_page, name='update_page'),
    path('delet-page/<int:pk>', views.delete_page, name='delete_page'),
]