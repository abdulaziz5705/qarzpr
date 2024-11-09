from django.urls import path


from app_users.views import RegisterView, LoginView, UserListView, UserDetailView, UserSearchView, AuthenticateUserView, \
    AuthenticatedSuperUserView, UnauthenticatedUserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/list/', UserListView.as_view(), name='usersearch'),
    path('users/detail/<int:pk>/', UserDetailView.as_view(), name='userdetail'),
    path('users/search/', UserSearchView.as_view(), name='usersearch'),
    path('authenticated/', AuthenticateUserView.as_view(), name='authenticated'),
    path('authenticated/admin/', AuthenticatedSuperUserView.as_view(), name='admin-authenticated'),
    path('unauthenticated/', UnauthenticatedUserView.as_view(), name='unauthenticated'),

]