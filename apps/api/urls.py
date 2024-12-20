from django.urls import path
from .views import AuthorAPIView
from .views import AuthorGenericAPIView
from django.urls import include
from .views import AuthorViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'authors_viewset', AuthorViewSet, basename='authors-viewset')

urlpatterns = [
    path('authors/', AuthorAPIView.as_view(), name='author-list'),
    path('authors_generic/', AuthorGenericAPIView.as_view(), name='author-generic-list'),
    path('authors_generic/<int:pk>/', AuthorGenericAPIView.as_view(), name='author-generic-detail'),
    path('authors/<int:pk>/', AuthorAPIView.as_view(), name='author-detail'),
    path('', include(router.urls)),
]