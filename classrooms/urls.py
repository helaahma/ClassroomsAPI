
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classes import views
from api.views import ClassesList, ClassesDetails, ClassesCreate, ClassesUpdate, ClassesCancel
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', views.classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom-detail'),

    path('classrooms/create', views.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', views.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', views.classroom_delete, name='classroom-delete'),
    path('list/', ClassesList.as_view(), name='class-list'),
    path('detail/<int:class_id>/', ClassesDetails.as_view(), name='class-details'),
    path('create/', ClassesCreate.as_view(), name='class-create'),
    path('class/<int:class_id>/update/', ClassesUpdate.as_view(), name='class-update'),
    path('class/<int:class_id>/delete/', ClassesCancel.as_view(), name='class-cancel'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
