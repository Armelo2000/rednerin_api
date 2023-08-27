
from django.urls import path, include
from . import views
#from .views import *

from rest_framework.routers import DefaultRouter

#router for class views
router = DefaultRouter()
router.register('rednerin', views.RednerinViewSet, basename='rednerin')
router.register('rednerinInfo', views.RednerinInfoViewSet, basename='rednerinInfo')
router.register('subject', views.SubjectViewSet, basename='subject')
router.register('url', views.UrlViewSet, basename='url')
router.register('socialnetwork', views.SocialNetworkViewSet, basename='socialnetwork')
router.register('video', views.VideoViewSet, basename='video')


urlpatterns = [

    path('user', views.user, name='users'),

    path('info', views.info, name='info'),

    path('test/<int:pk>', views.test, name='test'),

    path('', include(router.urls)),

]




