from django.db.models import Q
from collections import defaultdict
from users.models import Messaging
from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from django.contrib.auth.decorators import login_required
from users.models import Profile

@login_required
def message(request):
    # Get user profile for various later operations
    profile = request.user.profile
    
    # Handle selecting a conversation
    selected_profile = None
    conversation_with = request.GET.get('conversation_with')
    if conversation_with:
        selected_profile = get_object_or_404(Profile, id=conversation_with)
    
    # Process message sending
    if request.method == 'POST' and request.POST.get('action') == 'send':
        recipient_id = request.POST.get('recipient_id')
        sending_message = request.POST.get('sending_message')
        
        if recipient_id and sending_message:
            recipient_profile = get_object_or_404(Profile, id=recipient_id)
            
            message_entry = Messaging(
                sender_id=profile,
                receiver_id=recipient_profile,
                message_content=sending_message,
                sent_at=datetime.now(),
                read_status=False
            )
            message_entry.save()
            
            # If sending from modal, redirect to the new conversation
            if not selected_profile:
                return redirect(f"/messaging/message/?conversation_with={recipient_id}")
            
    # Get list of users for sending list - exclude current user
    all_profiles = Profile.objects.exclude(id=profile.id)
    user_list = [(p.id, p.user.username) for p in all_profiles]
    
    # Fetch messages related to the profile
    all_messages = Messaging.objects.filter(
        Q(sender_id=profile) | Q(receiver_id=profile)
    ).order_by('sent_at')
    
    # Dictionary to store messages grouped by non-profile user
    messages_dict = defaultdict(list)
    
    # Iterate through messages and group them by the other participant
    for msg in all_messages:
        other_user = msg.receiver_id if msg.sender_id == profile else msg.sender_id
        messages_dict[other_user].append(msg)
    
    # Add unread count for each conversation
    for other_user, msgs in messages_dict.items():
        unread_count = sum(1 for msg in msgs if msg.sender_id != profile and not msg.read_status)
        other_user.unread_count = unread_count
    
    # Mark messages as read if viewing a conversation
    if selected_profile and selected_profile in messages_dict:
        for msg in messages_dict[selected_profile]:
            if msg.receiver_id == profile and not msg.read_status:
                msg.read_status = True
                msg.save()
    
    # Convert defaultdict to a standard dict
    messages_by_user = dict(messages_dict)
    
    return render(request, 'messaging.html', {
        'messages_by_user': messages_by_user,
        'user_list': user_list,
        'selected_profile': selected_profile
    })
