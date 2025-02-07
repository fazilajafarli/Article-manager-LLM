from django.urls import path
from .views import ArticleSummaryView, ArticleListCreateView, ArticleDetailView

urlpatterns = [
    path('', ArticleListCreateView.as_view(), name='article-list-create'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('<int:pk>/summary/', ArticleSummaryView.as_view(), name='article-summary'),
]