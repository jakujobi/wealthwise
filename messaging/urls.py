from django.urls import path, include
from . import views

app_name = 'messaging'

# URLs for rendering chat pages
urlpatterns = [
    path('', views.conversation_list_view, name='conversation-list-page'), # Add URL for the list page
    path('chat/<int:conversation_id>/', views.chat_view, name='chat-view'),
]

# URLs for the API
api_urlpatterns = [
    path('conversations/', views.ConversationListView.as_view(), name='conversation-list'), # List all conversations for user
    path('conversations/<int:conversation_id>/messages/', views.MessageListView.as_view(), name='message-list'), # List messages in a specific conversation
    # TODO: Add URL for ConversationListView when implemented
    # path('conversations/', views.ConversationListView.as_view(), name='conversation-list'),
]

urlpatterns += [
    path('api/', include((api_urlpatterns, 'api'), namespace='api')),
]
