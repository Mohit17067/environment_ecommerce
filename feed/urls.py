from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    TagPostListView,
    ProviderPostListView,
    PostBidView,
    PostDonateView,
    BiddersListView,
    DonatorsListView,
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='feed-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('provider/<str:username>', ProviderPostListView.as_view(), name='provider-posts'),
    path('<str:text>', TagPostListView.as_view(), name='tag-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/bid', PostBidView.as_view(), name='post-bid'),
    path('post/<int:pk>/donate', PostDonateView.as_view(), name='post-donate'),
    path('post/<int:pk>/bidders', BiddersListView.as_view(), name='show-bidders'),
    path('post/<int:pk>/donators', DonatorsListView.as_view(), name='show-donators'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='feed-about'),
]