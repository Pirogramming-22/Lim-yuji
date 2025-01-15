from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'ideas'

urlpatterns = [
    path('', views.idea_list, name='list'),
    path('<int:pk>/', views.idea_detail, name='detail'),
    path('create/', views.idea_create, name='create'),
    path('<int:pk>/update/', views.idea_update, name='update'),
    path('<int:pk>/delete/', views.idea_delete, name='delete'),
    path('toggle-star/<int:pk>/', views.toggle_star, name='toggle_star'),
    path('update-interest/<int:pk>/', views.update_interest, name='update_interest'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])