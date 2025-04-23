from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, permissions
from .models import Conversation, Message, NotificationSetting
from .serializers import ConversationSerializer, MessageSerializer, NotificationSettingSerializer

# Create your views here.

@login_required
def index(request):
    conversations = request.user.conversations.all()
    return render(request, 'messaging/index.html', {'conversations': conversations})

class ConversationViewSet(viewsets.ModelViewSet):
    serializer_class = ConversationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.conversations.all()

    def perform_create(self, serializer):
        convo = serializer.save()
        convo.participants.add(self.request.user)
        return convo

class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Message.objects.filter(conversation__participants=self.request.user).order_by('timestamp')

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

class NotificationSettingViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSettingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.notification_settings.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
