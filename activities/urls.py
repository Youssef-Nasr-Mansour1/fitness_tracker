from django.urls import path
from .views import UserCreateView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ActivityViewSet
from .views import ActivityHistoryView, ActivityMetricsView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user_register'),
    path('history/', ActivityHistoryView.as_view(), name='activity_history'),
    path('metrics/', ActivityMetricsView.as_view(), name='activity_metrics'),
]

router = DefaultRouter()
router.register(r'activities', ActivityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]