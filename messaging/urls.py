from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import index, ConversationViewSet, MessageViewSet, NotificationSettingViewSet

router = DefaultRouter()
router.register(r'conversations', ConversationViewSet, basename='conversation')
router.register(r'messages', MessageViewSet, basename='message')
router.register(r'notification-settings', NotificationSettingViewSet, basename='notificationsetting')

urlpatterns = [
    path('', index, name='messaging_index'),
    path('api/', include(router.urls)),
]
