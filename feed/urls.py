from django.urls import path,include
from django.conf.urls import url
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
    BiddersListView,
    DonatorsListView,
    PostAssignView,
    PostCompleteView,
    PostFeedbackView,
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='feed-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('provider/<str:username>', ProviderPostListView.as_view(), name='provider-posts'),
    path('<str:text>', TagPostListView.as_view(), name='tag-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/bid', PostBidView.as_view(), name='post-bid'),
    path('post/<int:pk>/donate', views.donate_view, name='post-donate'),
    # path('post/process-payment/<int:service_id>/', views.payment_process, name='payment-process'),
    path('post/handle_payment/', views.handle_payment, name='handle-payment'), 
    path('post/<int:pk>/bidders', BiddersListView.as_view(), name='show-bidders'),
    path('post/<int:pk>/donators', DonatorsListView.as_view(), name='show-donators'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/assign/<int:bid_id>/', PostAssignView, name='post-assign'),
    path('post/<int:pk>/complete/', views.PostCompleteView, name='post-complete'),
    path('post/<int:pk>/feedback/', PostFeedbackView.as_view(), name='post-feedback'),
    path('about/', views.about, name='feed-about'),
    url(r'^ratings/', include(('star_ratings.urls','ratings'),namespace='ratings')),
]

