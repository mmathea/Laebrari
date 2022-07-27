"""
laebrari URL Configuration
"""

from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from rest_framework import routers
from django.urls import include, path
from user_library.views import BookTransactionViewSet, LibraryBookCreateView, LibraryBookViewSet, LibraryDetail, UserLibraryViewSet

from users.views import ProfileView, ProfileViewSet, UserViewSet, home, user_registration


router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename="user")
router.register(r'librarians', ProfileViewSet, basename="librarian")
router.register(r'libraries', UserLibraryViewSet, basename="library")
router.register(r'books', LibraryBookViewSet, basename="library_books")
router.register(r'transactions', BookTransactionViewSet, basename="book_transaction")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', user_registration, name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
    # add book to library
    path('book/add/', LibraryBookCreateView.as_view(), name='add_book'),
    # view book detail
    # view all public books
    # view library with book list
    path('api/', include(router.urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)