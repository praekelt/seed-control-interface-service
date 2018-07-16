from django.conf.urls import url, include
from rest_framework import routers
from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = [
    url(r'^api/v1/auditlog/', views.AuditLogList.as_view()),
]
