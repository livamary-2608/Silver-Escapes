from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .forms import CustomPasswordResetForm
urlpatterns = [
    path("",views.home,name="home"),
    path("login/",views.login_page,name="login"),
    path("contact/", views.contact, name="contact"),
    path("about/",views.about,name="about"),
    path("register/", views.register_page, name="register"),
    path("logout/", views.logout_page, name="logout"),
    path("faq/", views.faq, name="faq"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("destinations/", views.destinations, name="destinations"),
    path("itinerary/", views.itinerary, name="itinerary"),
    path("itinerary/edit/<int:id>/", views.edit_itinerary, name="edit_itinerary"),
    path("itinerary/delete/<int:id>/", views.delete_itinerary, name="delete_itinerary"),
    path(
    "destinations/<slug:slug>/",
    views.destination_detail,
    name="destination_detail"),
    path(
    "wishlist/<slug:slug>/",
    views.toggle_wishlist,
    name="toggle_wishlist"),
    path(
    "forgot-password/",
    auth_views.PasswordResetView.as_view(
    template_name="main/password_reset.html",
    form_class=CustomPasswordResetForm,
),
    name="password_reset"
),

path(
    "forgot-password/done/",
    auth_views.PasswordResetDoneView.as_view(
        template_name="main/password_reset_done.html"
    ),
    name="password_reset_done"
),

path(
    "reset/<uidb64>/<token>/",
    auth_views.PasswordResetConfirmView.as_view(
        template_name="main/password_reset_confirm.html"
    ),
    name="password_reset_confirm"
),

path(
    "reset/done/",
    auth_views.PasswordResetCompleteView.as_view(
        template_name="main/password_reset_complete.html"
    ),
    name="password_reset_complete"
),
path(
    "edit-profile/",
    views.edit_profile,
    name="edit_profile"
),
path(
    "remove-profile-picture/",
    views.remove_profile_picture,
    name="remove_profile_picture"
),
path(
    "destinations/<slug:slug>/hotels/",
    views.hotels,
    name="hotels",
),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
