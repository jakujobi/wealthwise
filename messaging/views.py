from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Q, Case, When, F, IntegerField
from django.http import JsonResponse, Http404
from django.utils import timezone
from .models import Message
import json

User = get_user_model()

@login_required
def inbox(request):
    user = request.user

    # 1. Find unique participant IDs
    participant_ids = Message.objects.filter(
        Q(sender=user) | Q(recipient=user)
    ).annotate(
        # Determine the other participant's ID for each message row
        other_user_id=Case(
            When(sender=user, then=F('recipient_id')),
            default=F('sender_id'),
            output_field=IntegerField()
        )
    ).values_list('other_user_id', flat=True).distinct() # Get unique IDs

    # 2. Get the latest message for each conversation
    latest_messages = []
    for p_id in participant_ids:
        try:
            # For each participant, find the latest message involving them and the user
            latest = Message.objects.filter(
                (Q(sender=user) & Q(recipient_id=p_id)) |
                (Q(sender_id=p_id) & Q(recipient=user))
            ).select_related('sender', 'recipient').latest('timestamp') # Use .latest()
            latest_messages.append(latest)
        except Message.DoesNotExist:
            # This should ideally not happen if participant_ids are derived correctly
            # but added for safety.
            continue

    # 3. Sort the collected latest messages by timestamp (most recent first)
    latest_messages.sort(key=lambda m: m.timestamp, reverse=True)

    # Get all users excluding the current user, for starting new conversations
    all_users = User.objects.exclude(id=user.id).order_by('username')

    context = {
        'message_details': latest_messages, # Pass the sorted list
        'all_users': all_users,
    }
    return render(request, 'messaging/inbox.html', context)


@login_required
def conversation_detail(request, user_id):
    other_user = get_object_or_404(User, id=user_id)
    if other_user == request.user:
        # Prevent users from messaging themselves
        raise Http404("You cannot start a conversation with yourself.")

    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Message.objects.create(
                sender=request.user,
                recipient=other_user,
                content=content
            )
            # Redirect back to the same conversation view after sending
            return redirect('messaging:conversation_detail', user_id=other_user.id)

    # Fetch messages between the logged-in user and the other user
    messages = Message.objects.filter(
        (Q(sender=request.user) & Q(recipient=other_user)) |
        (Q(sender=other_user) & Q(recipient=request.user))
    ).select_related('sender', 'recipient').order_by('timestamp')

    # Mark messages sent by the other user as read
    # Make sure to use the current user's perspective for marking read
    messages_to_mark_read = messages.filter(sender=other_user, recipient=request.user, is_read=False)
    if messages_to_mark_read.exists():
        messages_to_mark_read.update(is_read=True, read_at=timezone.now())

    context = {
        'other_user': other_user,
        'messages': messages,
    }
    return render(request, 'messaging/conversation_detail.html', context)

@login_required
def fetch_new_messages(request, user_id):
    if not request.accepts('application/json'):
        return JsonResponse({'error': 'Invalid request type'}, status=400)

    try:
        other_user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

    last_timestamp_str = request.GET.get('last_timestamp')
    # print(f"Received last_timestamp: {last_timestamp_str}") # Debugging

    queryset = Message.objects.filter(
        sender=other_user,
        recipient=request.user,
        is_read=False # Fetch only unread messages initially for notification/update purposes
    )

    # Optionally filter by timestamp if provided
    # if last_timestamp_str:
    #     try:
    #         # Ensure the timestamp is timezone-aware if your settings use timezones
    #         last_timestamp = timezone.datetime.fromisoformat(last_timestamp_str)
    #         if timezone.is_naive(last_timestamp) and timezone.is_aware(timezone.now()):
    #             last_timestamp = timezone.make_aware(last_timestamp, timezone.get_current_timezone())
    #         queryset = queryset.filter(timestamp__gt=last_timestamp)
    #         # print(f"Filtering timestamp > {last_timestamp}") # Debugging
    #     except ValueError:
    #         return JsonResponse({'error': 'Invalid timestamp format'}, status=400)

    new_messages = list(queryset.order_by('timestamp').values(
        'sender__username', 'content', 'timestamp', 'id'
    ))

    # Mark fetched messages as read after preparing the response
    if new_messages:
        message_ids = [msg['id'] for msg in new_messages]
        Message.objects.filter(id__in=message_ids).update(is_read=True, read_at=timezone.now())
        # print(f"Marked messages as read: {message_ids}") # Debugging

    # print(f"Returning {len(new_messages)} new messages.") # Debugging
    return JsonResponse({'messages': new_messages})


# Utility function (if needed, or integrate directly)
def get_last_message(user1, user2):
    try:
        return Message.objects.filter(
            (Q(sender=user1, recipient=user2) | Q(sender=user2, recipient=user1))
        ).latest('timestamp')
    except Message.DoesNotExist:
        return None
