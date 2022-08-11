from django.urls import path, include

from .api_router import router
from .views import IndexView, AboutView, LoginPageView, SignupView, LogoutView,CheckUserNameView 

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('about/', AboutView.as_view(), name="about"),
    path('login/', LoginPageView.as_view(), name="loginPage"),
    path('signup/', SignupView.as_view(), name="signup"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('api/', include(router.urls)),
    path("check_username/", CheckUserNameView.as_view(), name="check_user_name")
]
