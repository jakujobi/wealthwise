# messaging/urls.py
from django.urls import path
from . import views

app_name = 'messaging'

urlpatterns = [
    path('', views.inbox, name='inbox'), # e.g., /messages/
    path('conversation/<int:user_id>/', views.conversation_detail, name='conversation_detail'), # e.g., /messages/conversation/5/
    # path('send/<int:recipient_id>/', views.send_message, name='send_message'), # Remove this line - sending handled in conversation_detail POST
    path('api/fetch/<int:user_id>/', views.fetch_new_messages, name='fetch_new_messages'), # e.g., /messages/api/fetch/5/
]
