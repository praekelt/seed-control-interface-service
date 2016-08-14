from .models import UserDashboard, Dashboard
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import (UserDashboardSerializer, DashboardSerializer)


class DashboardViewSet(viewsets.ReadOnlyModelViewSet):

    """
    API endpoint that allows dashboard to be viewed
    """
    permission_classes = (IsAuthenticated,)
    queryset = Dashboard.objects.all()
    serializer_class = DashboardSerializer


class UserDashboardViewSet(viewsets.ReadOnlyModelViewSet):

    """
    API endpoint that allows user dashboard to be viewed
    """
    permission_classes = (IsAuthenticated,)
    queryset = UserDashboard.objects.all()
    serializer_class = UserDashboardSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filter_fields = ('user_id', )
