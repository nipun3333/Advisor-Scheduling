from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from django.urls import path
from . import views

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('user/register', views.RegisterView.as_view(), name="register"),
    path('admin/advisor', views.AdvisorView.as_view(), name="add_advisors"),
    path('user/login', views.LoginView.as_view(), name="login"),
    path('user/<int:userid>/advisor', views.allAdvisorView.as_view(), name="advisors"),
    path('user/<int:userid>/advisor/<int:advisorid>', views.bookView.as_view(), name="booking"),
    path('user/<int:userid>/advisor/booking', views.ScheduleView.as_view(), name="Schedule")
]
