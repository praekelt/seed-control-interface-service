from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register(r'changes', views.ChangeGetViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/auditlog/', views.AuditLogList.as_view()),
]
