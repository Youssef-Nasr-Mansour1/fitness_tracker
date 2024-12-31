from rest_framework import generics
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework import viewsets, permissions
from .models import Activity
from .serializers import ActivitySerializer
from rest_framework import views
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


class UserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def get_queryset(self):
        return Activity.objects.filter(user=self.request.user)


class ActivityHistoryView(generics.ListAPIView):
    serializer_class = ActivitySerializer

    def get_queryset(self):
        queryset = Activity.objects.filter(user=self.request.user)
        activity_type = self.request.query_params.get('activity_type', None)
        if activity_type:
            queryset = queryset.filter(activity_type=activity_type)
        return queryset


class ActivityMetricsView(views.APIView):

    def get(self, request):
        user_activities = Activity.objects.filter(user=request.user)
        total_duration = sum([activity.duration for activity in user_activities])
        total_distance = sum([activity.distance for activity in user_activities])
        total_calories = sum([activity.calories_burned for activity in user_activities])

        return Response({
            'total_duration': total_duration,
            'total_distance': total_distance,
            'total_calories': total_calories
        })


class CustomTokenObtainPairView(TokenObtainPairView):
    
    pass

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
