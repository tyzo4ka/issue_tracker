from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from api import views
from api.views import RegistrationView

router = routers.DefaultRouter()
router.register(r'projects', views.ProjectViewSet)
router.register(r'issues', views.IssueViewSet)
# router.register(r'register', views.RegistrationView)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("login/", obtain_auth_token, name="api_token_auth"),
    path("register/", RegistrationView.as_view(), name="api_register")
]
