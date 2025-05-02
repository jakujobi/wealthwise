# WealthWise Messaging Module

The Messaging module provides real-time communication capabilities between users in the WealthWise platform. It enables direct messaging between users with conversation tracking, read status, and a modern chat interface.

## Features

- **Private Messaging**: Direct messaging between any two users
- **Conversation Tracking**: Messages grouped by conversation partner
- **Read Status**: Track which messages have been read
- **Real-time Interface**: Modern chat-like interface for messaging
- **User Selection**: Easily select message recipients from a dropdown
- **Visual Notifications**: Unread message indicators

## Technical Implementation

### Backend

The messaging system is implemented using Django's Model-View-Template (MVT) architecture:

- **Models**: Uses the `Messaging` model from the `users` app
- **Views**: Implemented in `views.py` with the `message` view function
- **Template**: Uses `messaging.html` for the user interface

### File Structure

```
messaging/
├── __init__.py
├── templates/
│   └── messaging.html    # Main messaging interface template
├── templatetags/         # Custom template tags
│   ├── __init__.py
│   └── messaging_extras.py  # Contains custom template filters
├── urls.py               # URL configurations
├── views.py              # View logic
└── README.md             # This documentation
```

### Key Components

- **Message View Function**: Handles message display, filtering, and sending
- **Custom Template Tags**: Includes the `get_item` filter for dictionary access in templates
- **CSS Styling**: Modern, responsive design with animations and visual feedback

## Usage

1. **Accessing Messaging**: Click on the "Messages" link in the navigation bar
2. **Viewing Conversations**: Select a conversation from the left sidebar
3. **Sending Messages**: Use the message input at the bottom of the conversation view
4. **Starting New Conversations**: Click the "New Message" button and select a recipient

## Code Example

Here's a simplified example of sending a message:

```python
message_entry = Messaging(
    sender_id=request.user.profile,
    receiver_id=recipient_profile,
    message_content=message_text,
    sent_at=datetime.now(),
    read_status=False
)
message_entry.save()
```

## Future Enhancements

- Real-time updates using WebSockets
- Message status indicators (sent, delivered, read)
- File and image attachments
- Group messaging capabilities
- Message search functionality
