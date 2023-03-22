from django.urls import path
from socialweb import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns= [
path("signup",views.SignUpView.as_view(),name="register"),
path("login",views.LoginView.as_view(),name="signin"),
path("home",views.IndexView.as_view(),name="index"),
# path("profile/create",views.ProfileDView.as_view(),name="profile"),
path("posts/<int:id>/comments/add",views.AddCommentView.as_view(),name="add-comment"),
path("comments/<int:id>/upvote/add",views.UpvoteView.as_view(),name="upvote_add"),
path("comments/<int:id>/upvote/remove",views.UpvoteRemoveView.as_view(),name="upvote_remove"),
path("profiles/add",views.ProfileCreateView.as_view(),name="profile-add"),
path("profiles/details",views.ProfileView.as_view(),name="profile-details"),
path("profiles/<int:id>/change",views.ProfileEditView.as_view(),name="profile-edit"),
path("questions/<int:pk>/remove",views.PostsDeleteView.as_view(),name="post-delete"),
path("logout",views.SignOutView.as_view(),name="signout"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

