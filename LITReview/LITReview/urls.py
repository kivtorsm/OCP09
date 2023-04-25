"""
URL configuration for LITReview project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import authentication.views
import reviews.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentication.views.LoginPageView.as_view(), name='login'),
    path('logout/', authentication.views.logout_user, name='logout'),
    path('home/', reviews.views.home, name='home'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('posts/', reviews.views.posts, name='posts'),
    path('follows/', reviews.views.follows, name='follows'),
    path('user_follows_<int:user_follows_id>/unfollow/', reviews.views.unfollow, name='unfollow'),
    path('posts/new_ticket/', reviews.views.new_ticket, name='new_ticket'),
    path('posts/ticket_<int:ticket_id>/edit_ticket/', reviews.views.edit_ticket, name='edit_ticket'),
    path('posts/ticket_<int:ticket_id>/delete_ticket/', reviews.views.delete_ticket, name='delete_ticket'),
    path(
        'posts/create_ticket_plus_review/', reviews.views.create_ticket_plus_review, name='create_ticket_plus_review'),
    path('posts/review_<int:review_id>/edit_review/', reviews.views.edit_review, name='edit_review'),
    path('posts/review_<int:review_id>/delete_review/', reviews.views.delete_review, name='delete_review'),
    path('posts/ticket_<int:ticket_id>/create_review/', reviews.views.create_review, name='create_review'),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
