from django.urls import path, include
from .views import BecasViewSet, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('becas',BecasViewSet, basename='becas')
router.register('users',UserViewSet)



urlpatterns = [
    path('api/', include(router.urls)),

    #path('becas/', views.becas_list),
    #path('crear/', views.crear_beca),
    #path('editar/<str:pk>', views.editarbeca),
   #path('borrar/<str:pk>', views.borrarbeca),
    #path('becas/', BecasList.as_view()),
    #path('detalle/<str:id>', BecaDetalle.as_view()),
]