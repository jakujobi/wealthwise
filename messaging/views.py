from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import generics, permissions
from .models import Conversation, Message
from .serializers import MessageSerializer, ConversationSerializer
from django.db.models import Q
from django.contrib.auth import get_user_model

User = get_user_model()

# Page Rendering Views
@login_required
def conversation_list_view(request):
    """Renders the page that lists user's conversations."""
    # The template will use JavaScript to fetch the list via the API
    return render(request, 'messaging/conversation_list.html')

@login_required
def chat_view(request, conversation_id):
    """Renders the chat page for a specific conversation."""
    # Check if the user is a participant
    conversation = get_object_or_404(Conversation, id=conversation_id)
    if request.user not in conversation.participants.all():
        # Handle unauthorized access, e.g., redirect or show an error
        # For simplicity, we'll just return an empty context for now, 
        # but a proper redirect or error page is recommended.
        return render(request, 'messaging/unauthorized.html') 
        
    context = {
        'conversation_id': conversation_id,
        'user_id': request.user.id # Pass user ID for frontend logic
    }
    return render(request, 'messaging/chat.html', context)

# Placeholder for ConversationList view (we might need a specific Conversation serializer later)
# For now, let's focus on retrieving messages for a known conversation ID.

class MessageListView(generics.ListAPIView):
    """Lists messages for a specific conversation."""
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        conversation_id = self.kwargs.get('conversation_id')
        user = self.request.user

        # Ensure the user is part of the conversation
        try:
            conversation = Conversation.objects.get(id=conversation_id)
            if user not in conversation.participants.all():
                return Message.objects.none() # Return empty if user not participant
        except Conversation.DoesNotExist:
            return Message.objects.none() # Return empty if conversation doesn't exist

        return Message.objects.filter(conversation_id=conversation_id).order_by('timestamp')

class ConversationListView(generics.ListAPIView):
    """Lists conversations for the currently authenticated user."""
    serializer_class = ConversationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Order by most recent activity (requires adding a timestamp field to Conversation or querying latest message)
        # For simplicity, ordering by creation date for now.
        return Conversation.objects.filter(participants=user).order_by('-created_at')

# TODO: Add a view to list conversations for the user
# class ConversationListView(generics.ListAPIView):
#     serializer_class = ConversationSerializer # Need to create this
#     permission_classes = [permissions.IsAuthenticated]
#
#     def get_queryset(self):
#         user = self.request.user
#         return Conversation.objects.filter(participants=user) 