# Messaging Module

The Messaging module enables direct communication between users within the WealthWise platform, facilitating client-advisor interactions and user collaboration.

## Overview

The messaging system provides a real-time chat interface that allows users to:
- Send and receive private messages
- View message history by conversation
- Track read/unread message status
- Initiate new conversations with any platform user

## Architecture

The messaging feature is built using Django's Model-View-Template (MVT) architecture:

### Models

The messaging system uses the `Messaging` model defined in the `users` app:

```python
class Messaging(models.Model):
    sender_id = models.ForeignKey('users.Profile', related_name='sender', on_delete=models.CASCADE)
    receiver_id = models.ForeignKey('users.Profile', related_name='receiver', on_delete=models.CASCADE)
    message_content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    read_status = models.BooleanField(default=False)
```

### Views

The main view function in `messaging/views.py` handles:
- Loading and displaying conversations
- Sending new messages
- Updating read status
- User selection for new conversations

```python
@login_required
def message(request):
    # Get current user profile
    profile = request.user.profile
    
    # Handle conversation selection
    selected_profile = None
    conversation_with = request.GET.get('conversation_with')
    if conversation_with:
        selected_profile = get_object_or_404(Profile, id=conversation_with)
    
    # Process message sending
    if request.method == 'POST' and request.POST.get('action') == 'send':
        # Message sending logic...
    
    # Fetch and group messages by conversation partner
    all_messages = Messaging.objects.filter(
        Q(sender_id=profile) | Q(receiver_id=profile)
    ).order_by('sent_at')
    
    # Group messages by other participant
    messages_dict = defaultdict(list)
    for msg in all_messages:
        other_user = msg.receiver_id if msg.sender_id == profile else msg.sender_id
        messages_dict[other_user].append(msg)
    
    # Mark messages as read when viewing conversation
    if selected_profile and selected_profile in messages_dict:
        for msg in messages_dict[selected_profile]:
            if msg.receiver_id == profile and not msg.read_status:
                msg.read_status = True
                msg.save()
```

### Templates

The UI is defined in `messaging/templates/messaging.html` with these components:
- Two-column layout (conversation list and message display)
- Message composition form
- Modal for starting new conversations
- CSS animations and styling for an engaging user experience

## User Flow

1. User navigates to the messaging section via the "Messages" link in the navigation bar
2. The system loads all conversations for the current user
3. User selects a conversation from the sidebar or starts a new one
4. The selected conversation's messages appear in the main panel
5. User can type and send new messages using the composition form

## Template Tags

The messaging system uses a custom template tag module (`messaging_extras.py`) that provides:

```python
@register.filter
def get_item(dictionary, key):
    """
    Custom template filter to access dictionary items by key.
    Usage: {{ dictionary|get_item:key }}
    """
    return dictionary.get(key, [])
```

## Security Considerations

- All messaging routes require authentication (`@login_required` decorator)
- Message access is restricted to the sender and recipient
- Input validation prevents SQL injection and XSS attacks
- User IDs are properly validated before database operations

## Future Enhancements

- Real-time messaging with WebSockets
- Message delivery and read receipts
- File/image attachments
- Message searching and filtering
- Group messaging functionality
